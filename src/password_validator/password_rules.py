from abc import ABC, abstractmethod


class PasswordRule(ABC):
    @abstractmethod
    def ensure(self, password: str) -> str | None:
        pass

class MinimumLengthPasswordRule(PasswordRule):
    def __init__(self, length: int) -> None:
        self.length = length

    def ensure(self, password: str) -> str | None:
        if len(password) < self.length:
            return f"Password must be at least {self.length} characters long"
        return None

class UppercaseLetterPasswordRule(PasswordRule):
    def ensure(self, password: str) -> str | None:
        if password.lower() == password:
            return "Password must contain at least one uppercase letter"
        return None

class LowercaseLetterPasswordRule(PasswordRule):
    def ensure(self, password: str) -> str | None:
        if password.upper() == password:
            return "Password must contain at least one lowercase letter"
        return None

class DigitPasswordRule(PasswordRule):
    def ensure(self, password: str) -> str | None:
        if not any(char.isdigit() for char in password):
            return "Password must contain at least one digit"
        return None

class SpecialCharacterPasswordRule(PasswordRule):
    def ensure(self, password: str) -> str | None:
        import re
        if not re.findall(r'[!*_$&\-;,]+', password):
            return "Password must contain at least one special character"
        return None