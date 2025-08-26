from returns.result import Result, Failure


class Password:
    @classmethod
    def of(cls, password: str) -> Result["Password", list[str]]:
        if len(password) < 8:
            return Failure(["Password must be at least 8 characters long"])
        raise NotImplementedError()
