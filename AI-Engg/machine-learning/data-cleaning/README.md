# Airbnb Open Data --- Data Cleaning Project

## 1. Project Overview

This project cleans an Airbnb listings dataset using **Python and
Pandas**. The input file is `Airbnb_Open_Data.csv`. The notebook
inspects the data, removes unnecessary columns and incomplete records,
standardizes selected values, converts price strings into integers, and
exports the cleaned dataset to CSV and Excel formats.

The main goal is to turn a raw dataset into a more consistent table that
is easier to inspect, analyze, visualize, or prepare for later
data-science work.

> **Scope:** This notebook performs data cleaning and export. It does
> not train a machine-learning model, predict prices, or build a
> dashboard.

## 2. Problem Statement

Raw datasets commonly contain fields that are not needed for a
particular task, duplicate rows, missing values, inconsistent text, and
numeric values stored as strings. These issues can make analysis
unreliable or inconvenient.

In this project, the Airbnb dataset includes listing and host
information such as neighbourhood, room type, booking availability,
cancellation policy, construction year, price, service fee, minimum
nights, and review counts. Some fields are removed, missing-data rows
are dropped, and selected fields are transformed into more usable
formats.

### What this project aims to do

-   Load the raw Airbnb CSV file into a Pandas DataFrame.
-   Inspect the dataset's columns, structure, and sample records.
-   Remove columns considered unnecessary for this version of the
    project.
-   Rename `NAME` to `Name`.
-   Remove duplicate rows.
-   Remove the `last review` column and rows containing remaining
    missing values.
-   Standardize `host_identity_verified` text to uppercase.
-   Convert `instant_bookable` values into numeric flags (`1` or `0`).
-   Clean price strings by removing `$`, commas, and spaces, then
    convert prices to integers.
-   Save the cleaned data to CSV and Excel files.

## 3. Packages and Tools

### Required package

  -----------------------------------------------------------------------
  Package / tool                      Why it is used
  ----------------------------------- -----------------------------------
  **Pandas** (`pandas`)               Reads CSV files, stores tabular
                                      data in a DataFrame, inspects
                                      columns and data types,
                                      detects/removes duplicates and
                                      missing values, transforms columns,
                                      and exports CSV/Excel files.

  **Python**                          Runs the data-cleaning instructions
                                      and type conversions.

  **Jupyter Notebook**                Organizes the work into executable
                                      cells and displays intermediate
                                      tables and results.
  -----------------------------------------------------------------------

The notebook installs Pandas with `%pip install pandas` and imports it
as `pd`:

``` python
import pandas as pd
data = pd.read_csv("Airbnb_Open_Data.csv")
```

No NumPy, Matplotlib, Seaborn, scikit-learn, or machine-learning package
is explicitly imported in the notebook. Pandas may rely on NumPy
internally, but this script does not use NumPy directly.

**Excel export note:** `DataFrame.to_excel()` generally requires an
Excel-writing engine, commonly `openpyxl` for `.xlsx` files. If the
final export raises an engine-related error, install it in the same
environment:

``` bash
python -m pip install openpyxl
```

## 4. Input and Output Files

### Input

-   `Airbnb_Open_Data.csv` --- the source dataset. It must be available
    in the notebook's working directory, or the code must be updated
    with its correct path.

### Outputs

-   `Cleaned_Data.csv` --- an intermediate CSV export created before the
    later index-column cleanup. Because `to_csv()` is initially called
    with its default `index=True`, this file includes a saved DataFrame
    index.
-   `Cleaned_Data_Without_Index.csv` --- the intended cleaned CSV
    output. The notebook writes this file with `index=False`, so Pandas
    does not add an extra index column during export.
-   `Cleaned_Data_Without_Index.xlsx` --- an Excel workbook containing
    the cleaned data, also exported with `index=False`.

The notebook writes `Cleaned_Data_Without_Index.csv` more than once:
first before removing the `index` column that was created by
`reset_index()`, and then again after that column is dropped. The
**final write** is the version intended to be used.

## 5. Cleaning Workflow and Approach

The notebook follows this sequence:

1.  **Load and inspect:** Read the CSV, view the first rows, inspect
    column names, and check DataFrame information.
2.  **Choose relevant columns:** Define `column_to_keep` and
    `column_to_drop`. The notebook creates a filtered DataFrame called
    `df`, but the subsequent cleaning pipeline continues on `data`;
    therefore, `df` is an example/unused intermediate rather than the
    final dataset.
3.  **Remove unnecessary columns:** Drop `reviews per month`,
    `review rate number`, `calculated host listings count`,
    `availability 365`, `house_rules`, `license`, and `id`.
4.  **Rename a column:** Rename `NAME` to `Name` for a more readable
    column label.
5.  **Remove duplicate records:** Use `duplicated()` to inspect
    duplicates and `drop_duplicates()` to remove them.
6.  **Handle missing values:** Drop `last review`, check missing-value
    counts, and then use `dropna()` to remove rows that still contain
    missing values in the remaining columns.
7.  **Normalize text:** Convert `host_identity_verified` values to
    uppercase so values such as `verified` and `VERIFIED` use a
    consistent representation.
8.  **Encode a Boolean field:** Convert `instant_bookable` to `1` when
    the value compares equal to Python `True`, otherwise `0`.
9.  **Reset and clean the index:** Call `reset_index()`, which creates
    an `index` column, and later remove that column before the final
    export.
10. **Clean price formatting:** Remove dollar signs, commas, and spaces
    from `price`, then convert the resulting strings to integers.
11. **Export and verify:** Save the final DataFrame to CSV and Excel and
    read the CSV back to check the exported table.

### Why these transformations matter

-   **Dropping irrelevant columns** makes the working dataset smaller
    and more focused.
-   **Removing duplicates** reduces repeated records that could distort
    later counts or summaries.
-   **Handling missing values** avoids leaving nulls in the retained
    rows, although dropping rows can reduce the dataset considerably.
-   **Standardizing text** makes category values more consistent for
    grouping and filtering.
-   **Converting Boolean and price fields** makes those columns easier
    to use in calculations and later analysis.
-   **Exporting without the DataFrame index** avoids an unintended extra
    index column in the final files.

## 6. What the Final Output Means

The final `data` DataFrame represents the rows retained after the
notebook's cleaning steps. Its columns contain listing and host
attributes retained by the script, with these important changes:

-   `Name` is the renamed listing-name field.
-   `host_identity_verified` is uppercase text.
-   `instant_bookable` is represented as integer flags: `1` for values
    equal to `True`, and `0` otherwise.
-   `price` is an integer after removal of currency symbols, commas, and
    spaces.
-   The `index` helper column created by `reset_index()` is removed
    before the final export.
-   Rows with missing values in any remaining column are removed by
    `dropna()`.

The notebook's displayed intermediate DataFrame contains **99,342 rows**
after its cleaning steps. This is the number shown in the saved notebook
output; the exact count can differ if the input CSV changes.

The price values are converted to integers, but the notebook does not
explicitly validate the currency, check whether every price is
plausible, or handle malformed price values with `errors="coerce"`. The
output should therefore be understood as a cleaned dataset according to
these rules---not as proof that every record is accurate or every
missing value has been handled optimally.

## 7. How to Run the Project

1.  Put `Notebook.ipynb` and `Airbnb_Open_Data.csv` in the same working
    directory.

2.  Open the notebook in Jupyter Notebook or JupyterLab.

3.  Run the cells from top to bottom.

4.  If needed, install the dependencies:

    ``` bash
    python -m pip install pandas openpyxl
    ```

5.  Confirm that the CSV input path is correct.

6.  After the final cells run successfully, look for
    `Cleaned_Data_Without_Index.csv` and
    `Cleaned_Data_Without_Index.xlsx` in the notebook's working
    directory.

If using a virtual environment, activate it before installing packages
or launching Jupyter so the notebook runs in the intended Python
environment.

## 8. Important Limitations and Possible Improvements

This README documents what the current notebook does. The following are
potential improvements, not steps already implemented:

-   **Avoid dropping every row with any missing value without assessing
    impact.** Report missingness first, then decide column by column
    whether to drop, fill, or retain null values.
-   **Make Boolean conversion robust.** The current expression treats
    anything other than a value equal to `True` as `0`. If values arrive
    as strings such as `"True"` and `"False"`, they should be normalized
    explicitly.
-   **Use a safer price conversion.** Remove formatting, strip
    whitespace, use `pd.to_numeric(..., errors="coerce")`, and inspect
    values that fail conversion before choosing how to handle them.
-   **Avoid unnecessary index resets.** `reset_index()` creates an extra
    column unless `drop=True` is used. If the old index is not data,
    `data.reset_index(drop=True, inplace=True)` is simpler.
-   **Remove unused intermediate code.** The `column_to_keep` / `df`
    filtering example and uppercase-column-copy example are not used by
    the final pipeline. Remove them or clearly label them as
    demonstrations.
-   **Use explicit validation checks.** Compare row counts before and
    after cleaning, confirm expected column types, check duplicate
    counts, and verify output files.
-   **Make the script reproducible.** Define the input/output paths and
    cleaning steps in a reusable Python script or function, and record
    the cleaning decisions.

## 9. Summary

This is a beginner-friendly **Pandas data-cleaning project** using an
Airbnb listings dataset. It demonstrates how to inspect a dataset,
remove selected columns and duplicates, handle missing values, normalize
text, convert Boolean-like and price fields, and export a cleaner table.
Its result is a prepared dataset for future exploratory data analysis or
further processing; it does not itself answer a specific business
question such as which neighbourhood is cheapest or what determines
listing price.
