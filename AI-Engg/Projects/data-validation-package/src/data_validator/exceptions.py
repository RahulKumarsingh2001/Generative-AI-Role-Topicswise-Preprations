class DataValidatorError(Exception):
    """Base exception for the data_validator package."""


class UnsupportedFormatError(DataValidatorError):
    """Raised when a file format is unsupported."""


class DataReadError(DataValidatorError):
    """Raised when a file cannot be read or parsed."""