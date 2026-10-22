## What are you building?
```A reusable Python package that can read JSON and CSV files, 
validate their contents, and return clean, structured data with useful error messages.

example, you provide a CSV file containing user records. Your package reads it, checks whether required fields exist, 
validates data types, and reports invalid rows.
```


## Features to implement
```
Priority	    Feature	                              What we learn
1	            Read JSON files	                      json, file handling
2	            Read CSV files	                      csv, dictionaries
3	            Validate required fields	          Conditions, functions
4	            Validate data types	                  Type checking
5	            Handle malformed files	              Exceptions
6	            Return structured errors	          Classes, data structures
7	            Support reusable validation rules	  Functions, type hints
8	            Add automated tests	                  pytest
9	            Package for installation	          Python packaging
10	            Add documentation	                  Professional development practices
```


# Project structure
```
data-validator/
├── pyproject.toml
├── README.md
├── src/
│   └── data_validator/
│       ├── __init__.py
│       ├── readers.py
│       ├── validators.py
│       ├── exceptions.py
│       └── models.py
├── tests/
│   ├── test_readers.py
│   └── test_validators.py
└── examples/
    ├── users.json
    └── users.csv

```


