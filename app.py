import streamlit as st
import os

from dotenv import load_dotenv
from pypdf import PdfReader

import chromadb
from sentence_transformers import SentenceTransformer

import google.generativeai as genai


# --------------------------------------------------
# 1. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is missing. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)


# --------------------------------------------------
# 2. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Research Paper QA System",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# 3. SIMPLE PAGE APPEARANCE
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .title-box {
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        margin-bottom: 25px;
    }

    .title-box h1 {
        margin: 0;
        font-size: 32px;
    }

    .title-box p {
        margin-top: 8px;
        font-size: 16px;
    }

    .card {
        padding: 18px;
        border-radius: 10px;
        background-color: #f7f8fc;
        border: 1px solid #e5e7eb;
        margin-bottom: 18px;
    }

    .answer-box {
        padding: 18px;
        border-radius: 10px;
        background-color: #f7f8fc;
        border-left: 4px solid #667eea;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .source-box {
        padding: 10px 15px;
        border-radius: 8px;
        background-color: #f1f3f8;
        border: 1px solid #e5e7eb;
        margin-bottom: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# 4. TITLE
# --------------------------------------------------

st.markdown(
    """
    <div class="title-box">
        <h1>📄 Research Paper Question Answering System</h1>
        <p>Upload a research paper and ask questions about its contents.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# 5. LOAD EMBEDDING MODEL
# --------------------------------------------------

@st.cache_resource
def load_embedding_model():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    return model


embedding_model = load_embedding_model()


# --------------------------------------------------
# 6. CREATE CHROMA DATABASE
# --------------------------------------------------

@st.cache_resource
def create_database():

    client = chromadb.Client()

    collection = client.get_or_create_collection(
        name="research_papers"
    )

    return collection


collection = create_database()


# --------------------------------------------------
# 7. PDF UPLOAD
# --------------------------------------------------

st.subheader("📤 Upload Research Paper")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


# --------------------------------------------------
# 8. EXTRACT TEXT FROM PDF
# --------------------------------------------------

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    pages = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            pages.append(
                {
                    "page": page_number + 1,
                    "text": text
                }
            )


    # --------------------------------------------------
    # DOCUMENT INFORMATION
    # --------------------------------------------------

    st.markdown(
        """
        <div class="card">
        <b>📑 Document Information</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("📄 **File:**", uploaded_file.name)

    with col2:
        st.write("📃 **Pages:**", len(pages))


    # --------------------------------------------------
    # CHUNK THE TEXT
    # --------------------------------------------------

    chunks = []

    chunk_size = 1000

    chunk_overlap = 200


    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            if chunk_text.strip():

                chunks.append(
                    {
                        "text": chunk_text,
                        "page": page["page"]
                    }
                )

            start = end - chunk_overlap


    st.write(
        f"🔹 **Text chunks created:** {len(chunks)}"
    )


    # --------------------------------------------------
    # CREATE EMBEDDINGS
    # --------------------------------------------------

    texts = []

    for chunk in chunks:

        texts.append(chunk["text"])


    embeddings = embedding_model.encode(
        texts
    ).tolist()


    # --------------------------------------------------
    # STORE DATA IN CHROMADB
    # --------------------------------------------------

    try:

        collection.delete(
            where={}
        )

    except:

        pass


    ids = []

    documents = []

    metadatas = []


    for i, chunk in enumerate(chunks):

        ids.append(
            str(i)
        )

        documents.append(
            chunk["text"]
        )

        metadatas.append(
            {
                "page": chunk["page"],
                "file_name": uploaded_file.name
            }
        )


    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


    st.success(
        "✅ Research paper processed successfully!"
    )


    # --------------------------------------------------
    # USER QUESTION
    # --------------------------------------------------

    st.subheader("💬 Ask a Question")

    question = st.text_input(
        "Enter your question:",
        placeholder="Example: What is the main objective of this research?"
    )


    if question:

        # --------------------------------------------------
        # CREATE QUESTION EMBEDDING
        # --------------------------------------------------

        question_embedding = embedding_model.encode(
            [question]
        ).tolist()


        # --------------------------------------------------
        # RETRIEVE RELEVANT CHUNKS
        # --------------------------------------------------

        results = collection.query(
            query_embeddings=question_embedding,
            n_results=5
        )


        retrieved_documents = results["documents"][0]

        retrieved_metadata = results["metadatas"][0]


        # --------------------------------------------------
        # CREATE CONTEXT
        # --------------------------------------------------

        context = ""


        for i in range(len(retrieved_documents)):

            context += (
                "\n\n"
                + "Page: "
                + str(retrieved_metadata[i]["page"])
                + "\n"
                + retrieved_documents[i]
            )


        # --------------------------------------------------
        # SEND CONTEXT TO GEMINI
        # --------------------------------------------------

        prompt = f"""
You are a research paper question answering assistant.

Answer the user's question ONLY using the
information provided in the context.

Do not use outside knowledge.

If the answer cannot be found in the context,
say:

"The answer could not be found in the uploaded
research paper."

Context:
{context}

User Question:
{question}

Give a clear and concise answer.
"""


        model = genai.GenerativeModel(
            "gemini-3.6-flash"
        )


        response = model.generate_content(
            prompt
        )


        # --------------------------------------------------
        # DISPLAY ANSWER
        # --------------------------------------------------

        st.subheader("🤖 Answer")

        st.markdown(
            f"""
            <div class="answer-box">
            {response.text}
            </div>
            """,
            unsafe_allow_html=True
        )


        # --------------------------------------------------
        # DISPLAY SOURCES
        # --------------------------------------------------

        st.subheader("📚 Sources")

        pages_used = set()


        for metadata in retrieved_metadata:

            pages_used.add(
                metadata["page"]
            )


        for page in sorted(pages_used):

            st.markdown(
                f"""
                <div class="source-box">
                📄 Page {page}
                </div>
                """,
                unsafe_allow_html=True
            )