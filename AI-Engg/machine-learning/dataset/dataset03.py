# Python data structures and dataset formats

records = [
    {"id": 1, "question": "What is RAG?"},
    {"id": 2, "question": "What are embeddings?"}
]

for record in records:
    print(record["question"])

    


# CSV — Comma-Separated Values
# - Stores tabular records. Learn delimiters, headers, quoting, encoding, escaping, and missing values.

# id,question
# 1,What is RAG?
# 2,What are embeddings?    




# JSON — JavaScript Object Notation
# - Stores objects and nested structures.
{
  "question": "What is RAG?",
  "source": "rag-guide.pdf"
}




# JSONL / NDJSON — JSON Lines
# Stores one complete JSON value per line. Common for large AI datasets and chat fine-tuning files
{"question":"What is RAG?","answer":"Retrieval-Augmented Generation."}
{"question":"What is an embedding?","answer":"A numerical representation of data."}



