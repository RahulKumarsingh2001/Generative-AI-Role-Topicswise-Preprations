from data_validator import read_data, validate_records


def main():
    records = read_data("examples/users.csv")

    result = validate_records(
        records,
        required_fields=["name", "email", "age"],
        field_types={
            "name": str,
            "email": str,
            "age": int,
        },
        coerce_types=True,
        custom_validators={
            "email": lambda value: (
                isinstance(value, str)
                and "@" in value
                and "." in value.split("@")[-1]
            )
        },
    )

    print("VALID RECORDS")
    for record in result.valid_records:
        print(record)

    print("\nINVALID RECORDS")
    for record in result.invalid_records:
        print(record)

    print("\nVALIDATION ERRORS")
    for error in result.errors:
        print(error)

    print("\nAll records valid:", result.is_valid)


if __name__ == "__main__":
    main()