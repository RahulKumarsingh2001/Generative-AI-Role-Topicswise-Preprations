# What is a dataset?
# A dataset is a collection of related data organized for analysis, processing, or training a model.

# Name	Age	Marks
# Rahul	22	85
# Amit	23	78
# Priya	21	92

# Rows: Individual records.
# Columns: Features or attributes.
# Values: The actual data stored in each column.



# Different types of datasets

# 1. Structured data
# Data arranged in rows and columns, such as CSV files, Excel sheets, and SQL tables.
# Example: Student records, employee salaries.

# 2. Unstructured data
# Data without a fixed tabular structure, such as PDFs, documents, images, and audio.
# Example: PDF documents used in a RAG chatbot.

# 3. Semi-structured data
# Data organized using keys, tags, or metadata, but not necessarily in a fixed table.
# Example: JSON API responses, XML documents.






# Create your first dataset in Python
students = [
    {"name": "Rahul", "age": 22, "marks": 85},
    {"name": "Amit", "age": 23, "marks": 78},
    {"name": "Priya", "age": 21, "marks": 92}
]

print(students, end="\n\n")
print(students[0], end="\n\n")

for student in students:
    print(student["name"], student["age"], student["marks"])

for student in students:
    if student["marks"] > 80:
        print(student["name"], "has scored more than 80 marks.")    