from dataclasses import dataclass

from returns.result import Result, Failure, Success


@dataclass
class Password:
    _value: str

    def __init__(self, value: str) -> None:
        self._value = value

    @classmethod
    def of(cls, password: str) -> Result["Password", list[str]]:
        if len(password) < 8:
            return Failure(["Password must be at least 8 characters long"])
        if not any(char.isupper() for char in password):
            return Failure(["Password must contain at least one uppercase letter"])

        return Success(Password(password))

    def __str__(self) -> str:
        return self._value
