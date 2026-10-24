import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Priya"],
    "age": [22, 23, 21],
    "marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)
print(df.describe())



# Operation	                 Code	                Purpose
# View first rows	         df.head()	            Inspect the dataset
# View dimensions	         df.shape	            Get rows and columns
# View column names	         df.columns	            Inspect available features
# View data types	         df.dtypes	            Check column types
# Summary statistics	     df.describe()	        Analyze numeric columns
# Check missing values	     df.isnull().sum()	    Find incomplete data
# Select a column	         df["marks"]	        Access one feature
# Filter records	         df[df["marks"] > 80]	Select matching rows





# Learn how to load a real dataset

#load from csv file
df = pd.read_csv("students.csv")
print(df.head())
print(df.shape)






#load from json file
df = pd.read_json("students.json")
print(df.head())



# RAG pipeline typically processes this data through the following stages:

#               1. Collect data
#               PDFs, CSVs, websites, documents
#                         |
#                         v
#               2. Clean and preprocess
#               Remove unwanted content and handle errors
#                         |
#                         v
#               3. Split into chunks
#               Break long documents into smaller sections
#                         |
#                         v
#               4. Generate embeddings
#               Convert text into numerical vectors
#                         |
#                         v
#               5. Store and retrieve
#               Use a vector database to find relevant content




