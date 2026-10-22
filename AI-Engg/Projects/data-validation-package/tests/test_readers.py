import json

import pytest

from data_validator import (
    DataReadError,
    UnsupportedFormatError,
    read_csv,
    read_data,
    read_json,
)


def test_read_json(tmp_path):
    file_path = tmp_path / "users.json"
    file_path.write_text(
        json.dumps([{"name": "Amit", "age": 25}]),
        encoding="utf-8",
    )

    assert read_json(file_path) == [{"name": "Amit", "age": 25}]


def test_read_csv(tmp_path):
    file_path = tmp_path / "users.csv"
    file_path.write_text(
        "name,age\nAmit,25\n",
        encoding="utf-8",
    )

    assert read_csv(file_path) == [{"name": "Amit", "age": "25"}]


def test_read_data_detects_json(tmp_path):
    file_path = tmp_path / "users.json"
    file_path.write_text('[{"name": "Amit"}]', encoding="utf-8")

    assert read_data(file_path) == [{"name": "Amit"}]


def test_missing_file():
    with pytest.raises(DataReadError, match="File not found"):
        read_json("missing.json")


def test_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid}", encoding="utf-8")

    with pytest.raises(DataReadError, match="Invalid JSON"):
        read_json(file_path)


def test_json_must_contain_list_of_objects(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text('{"name": "Amit"}', encoding="utf-8")

    with pytest.raises(DataReadError, match="list of objects"):
        read_json(file_path)


def test_unsupported_format():
    with pytest.raises(UnsupportedFormatError):
        read_data("users.txt")


def test_csv_with_extra_values(tmp_path):
    file_path = tmp_path / "invalid.csv"
    file_path.write_text("name,age\nAmit,25,extra\n", encoding="utf-8")

    with pytest.raises(DataReadError, match="more values"):
        read_csv(file_path)