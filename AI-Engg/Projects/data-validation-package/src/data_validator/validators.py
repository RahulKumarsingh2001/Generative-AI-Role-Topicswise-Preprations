from typing import Any, Callable

from .models import ValidationError, ValidationResult


Validator = Callable[[Any], bool]


def validate_records(
    records: list[dict[str, Any]],
    required_fields: list[str] | None = None,
    field_types: dict[str, type] | None = None,
    custom_validators: dict[str, Validator] | None = None,
    coerce_types: bool = False,
) -> ValidationResult:
    """
    Validate records against configurable rules.

    Args:
        records: List of dictionaries to validate.
        required_fields: Fields that must exist and not be None.
        field_types: Expected Python type for each field.
        custom_validators: Optional field-specific validation functions.
        coerce_types: Convert compatible values to their expected types.

    Returns:
        A ValidationResult containing valid records, invalid records,
        and validation errors.
    """
    required_fields = required_fields or []
    field_types = field_types or {}
    custom_validators = custom_validators or {}

    result = ValidationResult()

    for record_number, original_record in enumerate(records, start=1):
        record = original_record.copy()
        record_errors: list[ValidationError] = []

        # 1. Check required fields.
        for field_name in required_fields:
            if (
                field_name not in record
                or record[field_name] is None
                or record[field_name] == ""
            ):
                record_errors.append(
                    ValidationError(
                        record_number,
                        field_name,
                        "Required field is missing or empty.",
                    )
                )

        # 2. Check and optionally convert field types.
        for field_name, expected_type in field_types.items():
            if field_name not in record:
                continue

            value = record[field_name]

            if value is None:
                continue

            # bool is a subclass of int in Python, so reject it for int.
            if expected_type is int and isinstance(value, bool):
                type_is_valid = False
            else:
                type_is_valid = isinstance(value, expected_type)

            if not type_is_valid and coerce_types:
                try:
                    converted_value = expected_type(value)

                    if expected_type is int and isinstance(
                        converted_value, bool
                    ):
                        raise ValueError("Boolean is not an integer value")

                    record[field_name] = converted_value
                    value = converted_value

                    if expected_type is int and isinstance(value, bool):
                        type_is_valid = False
                    else:
                        type_is_valid = isinstance(value, expected_type)

                except (ValueError, TypeError, OverflowError):
                    type_is_valid = False

            if not type_is_valid:
                record_errors.append(
                    ValidationError(
                        record_number,
                        field_name,
                        f"Expected {expected_type.__name__}, "
                        f"received {type(value).__name__}.",
                    )
                )

        # 3. Run custom validators.
        for field_name, validator in custom_validators.items():
            if field_name not in record:
                continue

            value = record[field_name]

            # Avoid running custom validation on missing values.
            if value is None or value == "":
                continue

            try:
                is_valid = validator(value)
            except Exception:
                is_valid = False

            if not is_valid:
                record_errors.append(
                    ValidationError(
                        record_number,
                        field_name,
                        "Custom validation failed.",
                    )
                )

        # 4. Separate valid and invalid records.
        if record_errors:
            result.invalid_records.append(record)
            result.errors.extend(record_errors)
        else:
            result.valid_records.append(record)

    return result