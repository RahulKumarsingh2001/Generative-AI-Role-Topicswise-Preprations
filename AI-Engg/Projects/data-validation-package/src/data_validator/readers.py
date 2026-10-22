import csv
import json
from pathlib import Path
from typing import Any

from .exceptions import DataReadError, UnsupportedFormatError


def read_json(file_path: str | Path) -> list[dict[str, Any]]:
    """Read a JSON file containing a list of objects."""
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError as exc:
        raise DataReadError(f"File not found: {path}") from exc
    except PermissionError as exc:
        raise DataReadError(f"Permission denied: {path}") from exc
    except UnicodeDecodeError as exc:
        raise DataReadError(f"File is not valid UTF-8: {path}") from exc
    except json.JSONDecodeError as exc:
        raise DataReadError(
            f"Invalid JSON in {path}, line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        ) from exc
    except OSError as exc:
        raise DataReadError(f"Could not read {path}: {exc}") from exc

    if not isinstance(data, list):
        raise DataReadError("JSON must contain a list of objects.")

    if not all(isinstance(record, dict) for record in data):
        raise DataReadError(
            "Every item in the JSON list must be an object."
        )

    return data


def read_csv(file_path: str | Path) -> list[dict[str, Any]]:
    """Read a CSV file and return its rows as dictionaries."""
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file, strict=True)

            if reader.fieldnames is None:
                raise DataReadError("CSV file is empty or has no header.")

            if not reader.fieldnames or any(
                not name or not name.strip()
                for name in reader.fieldnames
            ):
                raise DataReadError(
                    "CSV headers must be non-empty."
                )

            if len(set(reader.fieldnames)) != len(reader.fieldnames):
                raise DataReadError(
                    "CSV contains duplicate column names."
                )

            records = []

            for row in reader:
                if None in row:
                    raise DataReadError(
                        f"CSV row {reader.line_num} has more values "
                        "than the header."
                    )

                if any(value is None for value in row.values()):
                    raise DataReadError(
                        f"CSV row {reader.line_num} has fewer values "
                        "than the header."
                    )

                records.append(dict(row))

            return records

    except FileNotFoundError as exc:
        raise DataReadError(f"File not found: {path}") from exc
    except PermissionError as exc:
        raise DataReadError(f"Permission denied: {path}") from exc
    except UnicodeDecodeError as exc:
        raise DataReadError(f"File is not valid UTF-8: {path}") from exc
    except csv.Error as exc:
        raise DataReadError(f"Invalid CSV in {path}: {exc}") from exc
    except OSError as exc:
        raise DataReadError(f"Could not read {path}: {exc}") from exc


def read_data(file_path: str | Path) -> list[dict[str, Any]]:
    """Automatically select the reader based on the file extension."""
    extension = Path(file_path).suffix.lower()

    if extension == ".json":
        return read_json(file_path)

    if extension == ".csv":
        return read_csv(file_path)

    raise UnsupportedFormatError(
        f"Unsupported file format '{extension}'. Use .json or .csv."
    )