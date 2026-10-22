from data_validator import validate_records


def test_all_records_valid():
    records = [
        {"name": "Amit", "age": 25},
        {"name": "Rahul", "age": 30},
    ]

    result = validate_records(
        records,
        required_fields=["name", "age"],
        field_types={"name": str, "age": int},
    )

    assert result.is_valid
    assert len(result.valid_records) == 2
    assert len(result.invalid_records) == 0
    assert len(result.errors) == 0


def test_missing_required_field():
    records = [{"name": "Priya"}]

    result = validate_records(
        records,
        required_fields=["name", "email"],
    )

    assert not result.is_valid
    assert len(result.invalid_records) == 1
    assert any(error.field_name == "email" for error in result.errors)


def test_invalid_field_type():
    records = [{"name": "Amit", "age": "twenty"}]

    result = validate_records(
        records,
        required_fields=["name", "age"],
        field_types={"name": str, "age": int},
    )

    assert not result.is_valid
    assert any(
        error.field_name == "age"
        and "Expected int" in error.message
        for error in result.errors
    )


def test_type_coercion():
    records = [{"name": "Amit", "age": "25"}]

    result = validate_records(
        records,
        required_fields=["name", "age"],
        field_types={"name": str, "age": int},
        coerce_types=True,
    )

    assert result.is_valid
    assert result.valid_records[0]["age"] == 25
    assert isinstance(result.valid_records[0]["age"], int)


def test_custom_validator():
    records = [
        {"email": "amit@example.com"},
        {"email": "invalid-email"},
    ]

    result = validate_records(
        records,
        required_fields=["email"],
        custom_validators={
            "email": lambda value: (
                isinstance(value, str)
                and "@" in value
                and "." in value.split("@")[-1]
            )
        },
    )

    assert len(result.valid_records) == 1
    assert len(result.invalid_records) == 1
    assert result.errors[0].field_name == "email"


def test_boolean_is_not_accepted_as_integer():
    records = [{"age": True}]

    result = validate_records(
        records,
        field_types={"age": int},
    )

    assert not result.is_valid


def test_original_records_are_not_modified():
    records = [{"age": "25"}]

    validate_records(
        records,
        field_types={"age": int},
        coerce_types=True,
    )

    assert records[0]["age"] == "25"