class UserError(Exception):
    def __init__(self, msg):
        self.msg = msg


class UserNotExistError(UserError):
    pass


class PasswordIncorrectError(UserError):
    pass


class EmailNotValidError(UserError):
    pass