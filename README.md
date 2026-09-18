# -Research-Paper-Question-Answering-System
The system uses a RAG architecture. The PDF is processed using PyPDF, divided into chunks, and converted into embeddings using Sentence Transformers. ChromaDB stores the embeddings. User questions are semantically matched with relevant chunks, which are sent to Gemini for context-grounded answers with source page numbers.
RESEARCH PAPER QUESTION ANSWERING SYSTEM USING RAG

ABSTRACT:
Research papers contain a large amount of technical an scientific information, making it difficult for users to quickly find specific information from lengthy documents. Reading an entire research paper to identify its objective, methodology, findings, datasets, or limitations can be time-consuming.
The Research Paper Question Answering System is a Generative AI-based application that allows users to upload a research paper in PDF format and ask questions about its contents. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded document before generating an answer.
The system first extracts text from the uploaded PDF using PyPDF. The extracted text is divided into smaller sections called chunks. These chunks are converted into numerical vector representations called embeddings using the Sentence Transformers model. The embeddings are stored in ChromaDB, which acts as the vector database.
When a user asks a question, the question is also converted into an embedding. The system performs semantic similarity search in ChromaDB to retrieve the most relevant text chunks. These retrieved chunks are provided as context to the Google Gemini language model. Gemini generates an answer based only on the retrieved context.
The system also displays the source page numbers from which the relevant information was retrieved. This helps improve transparency and reduces the possibility of unsupported answers.
INTRODUCTION
Research papers are an important source of knowledge in academic and scientific fields. However, research papers can be lengthy and contain complex information. Students, researchers, and professionals may need to search through many pages to find answers to specific questions.
Traditional document searching generally depends on keywords. For example, if a user searches for a particular word, the system looks for matching words in the document. This approach may fail when the question and the document use different words with similar meanings.
Generative AI and Large Language Models can understand natural language questions, but directly asking an LLM about an uploaded document may result in unsupported or hallucinated information if the model does not have access to the document's actual content.
To address this problem, the proposed system uses Retrieval-Augmented Generation (RAG).
RAG combines information retrieval with a Large Language Model. Instead of asking the LLM to answer using only its internal knowledge, the system first retrieves relevant information from the uploaded research paper. The retrieved information is then provided to the LLM as context.
The basic workflow is:
PDF → Text Extraction → Text Chunking → Embeddings → Vector Database → Semantic Retrieval → Gemini → Answer
PROBLEM STATEMENT
Reading and analyzing lengthy research papers manually can require significant time and effort. Users may want quick answers to questions such as:
•	What is the main objective of the research?
•	What methodology was used?
•	What dataset was used?
•	What are the main findings?
•	What are the limitations of the study?
A conventional keyword-based search may not understand the meaning of the question. At the same time, a general-purpose LLM may provide information that is not present in the uploaded paper.
Therefore, there is a need for a system that can:
1.	Accept research papers in PDF format.
2.	Extract their textual content.
3.	Retrieve information based on semantic meaning.
4.	Generate answers using the retrieved content.
5.	Avoid using unrelated external knowledge.
6.	Provide source page information for the answer.
OBJECTIVES
The main objectives of the project are:
5.1 PDF Upload
Allow users to upload research papers in PDF format.
5.2 Text Extraction
Extract readable text from the uploaded research paper.
5.3 Text Chunking
Divide the extracted text into smaller sections so that relevant information can be retrieved efficiently.
5.4 Semantic Embeddings
Convert text chunks into numerical vector representations using a Sentence Transformer model.
5.5 Vector Storage
Store the generated embeddings and corresponding text chunks in ChromaDB.
5.6 Semantic Search
Convert the user's question into an embedding and retrieve the most semantically relevant chunks.
5.7 Context-Grounded Generation
Provide retrieved document content as context to the Gemini language model.
5.8 Source Identification
Display the page numbers from which relevant information was retrieved.
5.9 Reduce Unsupported Answers
Instruct the language model to answer only using the retrieved context and return a suitable message when the answer cannot be found
SCOPE OF THE PROJECT
The system is designed to answer questions related to an uploaded research paper.
The current system supports:
•	PDF upload
•	Research paper text extraction
•	Page-level processing
•	Text chunking
•	Text embeddings
•	Vector database storage
•	Semantic similarity search
•	Retrieval of relevant chunks
•	Gemini-based answer generation
•	Source page display
The system can be useful for:
•	Students
•	Researchers
•	Academic users
•	Research assistants
•	Project teams
•	People reviewing technical papers
SYSTEM ARCHITECTURE
The architecture of the system can be represented as:
 
10. TECHNOLOGIES USED
10.1 Python
Python is used as the primary programming language.
It provides libraries for:
•	PDF processing
•	Natural language processing
•	Embeddings
•	Vector databases
•	Generative AI
•	Web application development
________________________________________
10.2 Streamlit
Streamlit is used to create the web-based user interface.
It provides components such as:
•	File uploader
•	Text input
•	Buttons
•	Headers
•	Success messages
•	Answer display
The application can be run locally using:
python -m streamlit run app.py
________________________________________
10.3 PyPDF
PyPDF is used to extract text from uploaded PDF documents.
The application reads the PDF page by page and extracts the available text.
Example:
reader = PdfReader(uploaded_file)

for page_number, page in enumerate(reader.pages):
    text = page.extract_text()
________________________________________
10.4 Sentence Transformers
The project uses the Sentence Transformers library to generate embeddings.
The model used in the application is:
all-MiniLM-L6-v2
It converts text into numerical vectors that represent the semantic meaning of the text.
________________________________________
10.5 ChromaDB
ChromaDB is used as the vector database.
It stores:
•	Text chunks
•	Embeddings
•	Document IDs
•	Page metadata
•	File names
The system uses ChromaDB to retrieve text chunks that are semantically similar to the user's question.
________________________________________
10.6 Google Gemini
Google Gemini is used as the Large Language Model.
The retrieved document chunks are provided to Gemini as context.
The model then generates the final answer based on the supplied context.
The application uses:
gemini-3.6-flash
________________________________________
10.7 python-dotenv
The python-dotenv library is used to load the Gemini API key from the .env file.
Example:
GEMINI_API_KEY=YOUR_API_KEY
This avoids placing the API key directly inside the Python source code.
________________________________________
11. SYSTEM REQUIREMENTS
11.1 Hardware Requirements
Minimum requirements:
•	Processor: Intel Core i3 or equivalent
•	RAM: 8 GB
•	Storage: At least 2 GB free space
•	Internet connection for Gemini API access
Recommended:
•	Processor: Intel Core i5 or higher
•	RAM: 8 GB or more
•	Stable internet connection
________________________________________
11.2 Software Requirements
•	Windows / Linux / macOS
•	Python 3.x
•	Visual Studio Code
•	Internet browser
•	Gemini API key
________________________________________
12. PROJECT STRUCTURE
The project has the following basic structure:
Research-Paper-QA/
 ── app.py
 ── .env
app.py
Contains the complete Streamlit application and RAG pipeline.
.env
Stores the Gemini API key.
venv/
Contains the project's Python virtual environment.
________________________________________
13. REQUIREMENTS
The main dependencies are:
streamlit
pypdf
chromadb
sentence-transformers
google-generativeai
python-dotenv
These libraries provide the main functionality required for the application.
________________________________________
14. METHODOLOGY
The methodology consists of two major phases:
Phase 1 – Document Processing
The research paper is processed and stored in the vector database.
Phase 2 – Question Answering
The user's question is converted into an embedding, relevant information is retrieved, and Gemini generates the answer.
________________________________________
15. DOCUMENT PROCESSING PIPELINE
Step 1: Upload PDF
The user uploads a research paper using the Streamlit file uploader.
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)
Only PDF files are accepted.
________________________________________
Step 2: Extract Text
The PDF is processed using PyPDF.
reader = PdfReader(uploaded_file)
The application loops through every page.
for page_number, page in enumerate(reader.pages):

    text = page.extract_text()
The extracted text is associated with its page number.
For example:
Page 1 → Extracted text
Page 2 → Extracted text
Page 3 → Extracted text
________________________________________
16. TEXT CHUNKING
Large documents cannot always be processed as one large piece of text.
Therefore, the extracted text is divided into smaller sections called chunks.
The application uses:
Chunk size = 1000 characters
Overlap = 200 characters
Example:
Chunk 1:
Characters 0–999

Chunk 2:
Characters 800–1799

Chunk 3:
Characters 1600–2599
The overlap helps preserve information that occurs around chunk boundaries.
Why is chunking required?
Chunking helps:
•	Manage large documents.
•	Improve retrieval.
•	Retrieve only relevant portions.
•	Provide focused context to the LLM.
________________________________________
17. EMBEDDINGS
After chunking, each text chunk is converted into an embedding.
The project uses:
all-MiniLM-L6-v2
An embedding is a numerical representation of the meaning of a piece of text.
For example:
Text:
"Machine learning is used for classification."
        ↓
Embedding Model
        ↓
Numerical Vector
The numerical vectors allow the system to compare the semantic similarity between text chunks and questions.
________________________________________
18. VECTOR DATABASE
The generated embeddings are stored in ChromaDB.
The system creates a collection:
collection = client.get_or_create_collection(
    name="research_papers"
)
For each chunk, the system stores:
•	ID
•	Text
•	Embedding
•	Page number
•	File name
Example:
ID: 1
Text: Research methodology...
Page: 4
File: research_paper.pdf
Embedding: [vector values]
________________________________________
19. SEMANTIC RETRIEVAL
When the user asks a question, the question is converted into an embedding.
question_embedding = embedding_model.encode(
    [question]
).tolist()
The question embedding is then compared with the stored document embeddings.
The system retrieves the top 5 relevant chunks:
results = collection.query(
    query_embeddings=question_embedding,
    n_results=5
)
Therefore, instead of searching only for exact words, the system searches for text that is semantically related to the question.
________________________________________
20. CONTEXT CREATION
The retrieved chunks are combined into a context.
The context contains:
Page number
+
Retrieved text
For example:
Page: 4
The proposed methodology uses...

Page: 7
The experimental results show...
This context is then passed to Gemini.
________________________________________
21. PROMPT ENGINEERING
The system uses a prompt that instructs Gemini to answer only using the retrieved context.
The main instructions are:
Answer the user's question ONLY using the
information provided in the context.

Do not use outside knowledge.
If the answer is not available, the system instructs the model to return:
The answer could not be found in the uploaded research paper.
This is an important part of the RAG design because it helps keep the answer grounded in the uploaded document.
________________________________________
22. GENERATION USING GEMINI
The retrieved context and user question are sent to the Gemini model.
The basic process is:
Retrieved Context
        +
User Question
        ↓
      Gemini
        ↓
Generated Answer
The generated answer is displayed in the Streamlit interface.
________________________________________
23. SOURCE PAGE IDENTIFICATION
The system stores page information as metadata.
Example:
metadatas.append(
    {
        "page": chunk["page"],
        "file_name": uploaded_file.name
    }
)
After generating the answer, the application extracts the page numbers from the retrieved chunks.
The interface displays:
Sources

Page 3
Page 5
Page 8
This allows the user to identify the relevant parts of the research paper.
________________________________________
24. USER INTERFACE
The application provides a simple web interface.
The main sections are:
Header
Displays:
Research Paper Question Answering System
Upload Section
Allows the user to select a PDF research paper.
Document Information
Displays:
•	Uploaded file name
•	Number of pages
•	Number of generated text chunks
Question Section
Provides a text box where the user can enter a question.
Example:
What is the main objective of this research?
Answer Section
Displays the generated answer.
Sources Section
Displays the relevant source page numbers.
________________________________________
25. APPLICATION WORKFLOW
The complete workflow is:
Step 1
User opens the application.
Step 2
User uploads a research paper in PDF format.
Step 3
PyPDF extracts text from the PDF.
Step 4
The extracted text is divided into chunks.
Step 5
Sentence Transformer generates embeddings for the chunks.
Step 6
The chunks and embeddings are stored in ChromaDB.
Step 7
User enters a question.
Step 8
The question is converted into an embedding.
Step 9
ChromaDB performs semantic retrieval.
Step 10
The top 5 relevant chunks are retrieved.
Step 11
Retrieved chunks are combined into context.
Step 12
Context and question are sent to Gemini.
Step 13
Gemini generates an answer.
Step 14
The answer is displayed to the user.
Step 15
Relevant source page numbers are displayed.
________________________________________
26. RAG ARCHITECTURE
RAG stands for:
Retrieval-Augmented Generation
It consists of two main components:
Retrieval
The retrieval component searches the uploaded document and finds relevant information.
In this project:
Sentence Transformers
        +
ChromaDB
are used for retrieval.
Generation
The generation component uses the retrieved information to generate a natural-language answer.
In this project:
Google Gemini
is used for generation.
Therefore:
RAG = Retrieval + Generation
________________________________________
27. WHY RAG IS USED
A direct LLM approach would be:
Question → LLM → Answer
The LLM may not have the actual content of the uploaded research paper available as context.
The RAG approach is:
Question
   ↓
Retrieve relevant document content
   ↓
Provide retrieved content to LLM
   ↓
Generate answer
This makes the answer more closely connected to the uploaded document.
________________________________________
28. DIFFERENCE BETWEEN KEYWORD SEARCH AND SEMANTIC SEARCH
Keyword Search
Keyword search looks for matching words.
Example:
Question:
"What dataset was used?"

Search:
"dataset"
It mainly depends on matching terms.
Semantic Search
Semantic search attempts to identify content with similar meaning.
For example:
Question:
"What dataset was used?"

Document:
"The experiments were conducted using the
CIFAR-10 image collection."
Even though the exact question wording may not appear in the document, the relevant meaning can be retrieved.
The project uses embeddings and ChromaDB for semantic retrieval.
________________________________________
29. HALLUCINATION REDUCTION
A major challenge with Generative AI systems is hallucination.
Hallucination occurs when an AI model generates information that is not supported by the available information.
The project attempts to reduce this problem through:
1.	Retrieval of relevant document chunks.
2.	Providing retrieved chunks as context.
3.	Explicitly instructing Gemini not to use outside knowledge.
4.	Providing a fallback response when the answer cannot be found.
5.	Displaying source page numbers.
The system does not guarantee that hallucinations are impossible, but these mechanisms help ground the response in the uploaded document.
________________________________________
30. SECURITY CONSIDERATIONS
The Gemini API key is stored in the .env file rather than directly inside the source code.
Example:
GEMINI_API_KEY=YOUR_API_KEY
The application loads the key using:
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
The .env file should not be publicly uploaded to GitHub.
A .gitignore file should include:
.env
venv/
__pycache__/
________________________________________
31. ERROR HANDLING
The application checks whether the Gemini API key exists.
If the key is missing, the application displays:
Gemini API key is missing. Please check your .env file.
The system also handles cases where ChromaDB may not have an existing collection state by using a safe deletion operation.
________________________________________
32. TESTING
Testing is performed to verify whether the system works correctly for different inputs.
Test Case 1: Valid PDF Upload
Input: Valid research paper PDF
Expected Result:
PDF is uploaded and processed successfully.
Result: Pass
________________________________________
Test Case 2: Invalid File Type
Input: Non-PDF file
Expected Result:
The file should not be accepted.
Result: Pass
________________________________________
Test Case 3: Valid Question
Input:
What is the main objective of the research?
Expected Result:
The system retrieves relevant chunks and generates an answer.
Result: Pass
________________________________________
Test Case 4: Methodology Question
Input:
What methodology was used in the research?
Expected Result:
Relevant methodology information should be retrieved.
Result: Pass
________________________________________
Test Case 5: Dataset Question
Input:
What dataset was used?
Expected Result:
The system should retrieve the relevant section and provide an answer if the dataset is mentioned.
Result: Pass
________________________________________
Test Case 6: Question Not Present in Paper
Input:
What is the weather today?
Expected Result:
The system should not use outside knowledge and should return the configured not-found response if the relevant information cannot be found.
Result: Pass
________________________________________
Test Case 7: Source Verification
Input: Any question related to the paper.
Expected Result:
Relevant source page numbers should be displayed.
Result: Pass
________________________________________
33. SAMPLE INPUT AND OUTPUT
Sample Input
User uploads:
research_paper.pdf
Then enters:
What is the main objective of this research?
Processing
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Question Embedding
 ↓
Top 5 Relevant Chunks
 ↓
Gemini
Sample Output
Answer:

The main objective of the research is to investigate
the proposed approach and evaluate its effectiveness
using the experimental methodology described in the paper.
Sources:
Page 2
Page 3
The exact answer depends on the uploaded research paper.
________________________________________
34. ADVANTAGES
The system provides several advantages:
1.	Reduces the time required to manually search research papers.
2.	Allows natural-language questions.
3.	Uses semantic retrieval instead of simple keyword matching.
4.	Retrieves relevant document sections.
5.	Uses an LLM to generate understandable answers.
6.	Provides source page information.
7.	Can work with different research papers.
8.	Provides a simple web interface.
9.	Uses RAG to ground responses in retrieved document content.
10.	Can be extended with additional features in the future.
________________________________________
35. LIMITATIONS
The current implementation has some limitations:
1.	It primarily supports PDF documents.
2.	Text extraction depends on the structure of the PDF.
3.	Scanned/image-only PDFs may not provide usable text without OCR.
4.	The quality of the answer depends on the quality of retrieved chunks.
5.	Very complex tables and figures may not be represented properly through simple text extraction.
6.	The application requires a Gemini API key.
7.	Internet access is required for Gemini API communication.
8.	The current system processes one uploaded paper at a time.
9.	The current retrieval configuration uses the top 5 retrieved chunks.
10.	The current interface does not provide advanced document management features.
________________________________________
36. FUTURE ENHANCEMENTS
The project can be enhanced in several ways.
36.1 Multiple Research Papers
Allow users to upload multiple research papers and ask questions across all documents.
36.2 OCR Support
Add Optical Character Recognition to process scanned research papers.
36.3 Better Chunking
Implement more advanced chunking based on:
•	Sections
•	Paragraphs
•	Headings
•	Sentences
36.4 Improved Retrieval
The system can be extended with:
•	Hybrid search
•	Metadata filtering
•	Re-ranking
•	Multi-query retrieval
36.5 Research Paper Summarization
Add automatic summaries for:
•	Abstract
•	Methodology
•	Results
•	Conclusion
•	Limitations
36.6 Citation Improvements
Instead of only displaying page numbers, the application could display the exact retrieved passages.
36.7 Conversation History
Allow users to ask follow-up questions while maintaining conversation context.
36.8 Comparison of Research Papers
Users could upload multiple papers and compare:
•	Methodologies
•	Datasets
•	Results
•	Limitations
•	Research gaps
36.9 Visualization
The system could generate visual summaries such as:
•	Research methodology diagrams
•	Dataset statistics
•	Research trend charts
________________________________________
37. EXPECTED OUTCOME
The expected outcome of the project is a functional web-based research paper question-answering application.
The application should allow a user to:
1.	Upload a research paper.
2.	Process its content.
3.	Ask natural-language questions.
4.	Retrieve relevant information.
5.	Generate context-grounded answers.
6.	View source page numbers.
The system demonstrates how Retrieval-Augmented Generation can be applied to academic document question answering.
________________________________________
38. CONCLUSION
The Research Paper Question Answering System Using RAG provides an efficient way to interact with research papers using natural language.
The system combines PDF text extraction, text chunking, semantic embeddings, vector search, and Generative AI.
The research paper is first converted into manageable text chunks. These chunks are transformed into embeddings and stored in ChromaDB. When the user asks a question, the system retrieves the most relevant chunks based on semantic similarity. These chunks are then provided as context to Gemini, which generates a natural-language answer.
The addition of source page information improves transparency by helping users identify where the retrieved information originated.
Overall, the project demonstrates the practical use of Retrieval-Augmented Generation, vector databases, embeddings, semantic search, and Large Language Models for research-paper analysis.

