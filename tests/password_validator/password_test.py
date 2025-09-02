import unittest

from returns.result import Success, Failure, Result

from password_validator.password import Password


class PasswordShould(unittest.TestCase):
    def test_be_valid(self):
        maybe_password = Password.of("Cul4soo!")

        match maybe_password:
            case Success(password):
                self.assertEqual(str(password), "Cul4soo!")
            case Failure(errors):
                self.fail(f"A success was expected but got a failure: {errors}")

    def test_require_a_minimum_length(self):
        maybe_password = Password.of("Cul4so!")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected but got a success")
            case Failure(errors):
                self.assertListEqual(["Password must be at least 8 characters long"], errors)

    def test_require_at_least_an_uppercase_letter(self):
        maybe_password = Password.of("cul4soo!")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected but got a success")
            case Failure(errors):
                self.assertListEqual(["Password must contain at least one uppercase letter"], errors)

    def test_require_at_least_an_lowercase_letter(self):
        maybe_password = Password.of("CUL4SOO!")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected but got a success")
            case Failure(errors):
                self.assertListEqual(["Password must contain at least one lowercase letter"], errors)

    def test_require_at_least_one_digit(self):
        maybe_password = Password.of("Culasoo!")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected but got a success")
            case Failure(errors):
                self.assertListEqual(["Password must contain at least one digit"], errors)

    def test_require_at_least_a_special_character(self):
        maybe_password = Password.of("Cul4sooo")

        match maybe_password:
            case Success(_):
                self.fail("A failure was expected but got a success")
            case Failure(errors):
                self.assertListEqual(["Password must contain at least one special character"], errors)