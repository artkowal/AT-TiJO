from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class LoginValidator(Validator):
    def __init__(self, login):
        self.login = login
        self.LOGIN_MIN_LENGTH = 4

    def is_valid(self):

        return bool(self.login) and len(self.login) >= self.LOGIN_MIN_LENGTH

        # if self.login is None or len(self.login) < self.LOGIN_MIN_LENGTH:
        # return False

        # regex = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{4,}$"
        # pattern = compile(regex)
        # matcher = pattern.match(self.password)

    def field_name(self):
        return RegisterFormFields.LOGIN