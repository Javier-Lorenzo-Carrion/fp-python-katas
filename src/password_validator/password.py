from returns.result import Result


class Password:
    @classmethod
    def of(cls, password: str) -> Result["Password", list[str]]:
        raise NotImplementedError()
