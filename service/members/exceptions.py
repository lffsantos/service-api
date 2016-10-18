

class MemberAlreadyExists(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        super(MemberAlreadyExists, self).__init__()


class MemberNotFound(Exception):
    def __init__(self, full_name=None, email=None):
        self.full_name = full_name
        self.email = email
        super(MemberNotFound, self).__init__()


class AuxModelAlreadyExists(Exception):
    def __init__(self, cls_name, key, value):
        self.key = key
        self.value = value
        self.cls_name = cls_name
        super(AuxModelAlreadyExists, self).__init__()


class AuxModelNotFound(Exception):
    def __init__(self, cls_name, msg=None):
        self.msg = msg
        self.cls_name = cls_name
        super(AuxModelNotFound, self).__init__()


class EmailValidationFailed(Exception):
    def __init__(self, email):
        self.email = email
        super(EmailValidationFailed, self).__init__(
            "Failed to validate email %s" % (self.email,)
        )


class InvalidValueError(Exception):
    def __init__(self, field_name, field_value, expected_type):
        self.field_name = field_name
        self.field_value = field_value
        self.expected = expected_type
        super(InvalidValueError, self).__init__(
            "Invalid column '{}' ; value was '{}' but expected '{}'".format(
                self.field_name, repr(self.field_value), self.expected
            )
        )


class InvalidArgument(Exception):
    def __init__(self, cls_name, field_name):
        self.field_name = field_name
        self.cls_name = cls_name
        super(InvalidArgument, self).__init__()