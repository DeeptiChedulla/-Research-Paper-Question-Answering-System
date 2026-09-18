# -Research-Paper-Question-Answering-System
The system uses a RAG architecture. The PDF is processed using PyPDF, divided into chunks, and converted into embeddings using Sentence Transformers. ChromaDB stores the embeddings. User questions are semantically matched with relevant chunks, which are sent to Gemini for context-grounded answers with source page numbers.
