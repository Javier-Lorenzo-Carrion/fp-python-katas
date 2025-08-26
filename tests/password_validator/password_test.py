import unittest

from returns.result import Success, Failure, Result

from password_validator.password import Password


class PasswordShould(unittest.TestCase):
    def test_require_a_minimum_length(self):
        maybe_password: Result[Password, list[str]] = Password.of("Cul4so!")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected")
            case Failure(errors):
                self.assertListEqual(["Password must be at least 8 characters long"], errors)
