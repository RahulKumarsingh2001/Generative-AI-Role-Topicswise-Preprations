from dataclasses import dataclass, field
from typing import Any


@dataclass
class ValidationError:
    record_number: int
    field_name: str
    message: str

    def __str__(self) -> str:
        return (
            f"Record {self.record_number}, "
            f"field '{self.field_name}': {self.message}"
        )


@dataclass
class ValidationResult:
    valid_records: list[dict[str, Any]] = field(default_factory=list)
    invalid_records: list[dict[str, Any]] = field(default_factory=list)
    errors: list[ValidationError] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.invalid_records) == 0