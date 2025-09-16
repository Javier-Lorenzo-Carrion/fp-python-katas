from dataclasses import dataclass

from returns.result import Result, Failure, Success
import re

from unicodedata import normalize


@dataclass
class Password:
    _value: str

    def __init__(self, value: str) -> None:
        self._value = value

    @classmethod
    def of(cls, password: str) -> Result["Password", list[str]]:
        maybe_errors = []

        maybe_errors.append(cls.ensure_minimum_length(8, password))
        if not any(char.isupper() for char in password):
            maybe_errors.append("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            maybe_errors.append("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            maybe_errors.append("Password must contain at least one digit")
        if not re.findall(r'[!*_$&\-;,]+', password):
            maybe_errors.append("Password must contain at least one special character")

        errors: list[str] = list(filter(lambda error: error is not None, maybe_errors))

        if errors:
            return Failure(errors)

        return Success(Password(password))

    def __str__(self) -> str:
        return self._value

    @classmethod
    def ensure_minimum_length(cls, length: int, password: str) -> str | None:
        if len(password) < length:
            return f"Password must be at least {length} characters long"
        return None

