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
        maybe_errors = [cls.ensure_minimum_length(8, password),
                        cls.ensure_at_least_one_uppercase_letter(password),
                        cls.ensure_at_least_one_lowercase_letter(password),
                        cls.ensure_at_least_one_digit(password),
                        cls.ensure_at_least_one_special_character(password)]

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

    @classmethod
    def ensure_at_least_one_uppercase_letter(cls, password: str) -> str | None:
        if password.lower() == password:
            return "Password must contain at least one uppercase letter"
        return None

    @classmethod
    def ensure_at_least_one_lowercase_letter(cls, password: str) -> str | None:
        if password.upper() == password:
            return "Password must contain at least one lowercase letter"
        return None

    @classmethod
    def ensure_at_least_one_digit(cls, password: str) -> str | None:
        if not any(char.isdigit() for char in password):
            return "Password must contain at least one digit"
        return None

    @classmethod
    def ensure_at_least_one_special_character(cls, password: str) -> str | None:
        if not re.findall(r'[!*_$&\-;,]+', password):
            return "Password must contain at least one special character"
        return None
