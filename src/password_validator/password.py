from dataclasses import dataclass

from returns.result import Result, Failure, Success


@dataclass
class Password:
    _value: str

    def __init__(self, value: str) -> None:
        self._value = value

    @classmethod
    def of(cls, password: str) -> Result["Password", list[str]]:
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            errors.append("Password must contain at least one uppercase letter")

        if errors:
            return Failure(errors)

        return Success(Password(password))

    def __str__(self) -> str:
        return self._value
