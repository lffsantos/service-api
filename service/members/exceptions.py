

class MemberAlreadyExists(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        super(MemberAlreadyExists, self).__init__()


class MemberNotFound(Exception):
    def __init__(self, email=None):
        self.email = email
        super(MemberNotFound, self).__init__()


class AuxModelAlreadyExists(Exception):
    def __init__(self, cls_name, key, value):
        self.key = key
        self.value = value
        self.cls_name = cls_name
        super(AuxModelAlreadyExists, self).__init__()


class AuxModelNotFound(Exception):
    def __init__(self, cls_name, key, value):
        self.key = key
        self.value = value
        self.cls_name = cls_name
        super(AuxModelNotFound, self).__init__()


class InvalidValueError(Exception):
    def __init__(self, field_name, field_value, expected_type, reason=None):
        self.field_name = field_name
        self.field_value = field_value
        self.expected = expected_type
        self.reason = reason
        if reason:
            msg = "Invalid %s, %s; value was %s" % (
                self.field_name, self.reason, self.field_value
            )
        else:
            msg = "Invalid column '{}' ; value was '{}' but expected '{}'".format(
                self.field_name, repr(self.field_value), self.expected
            )
        super(InvalidValueError, self).__init__(msg)


class InvalidKeyConstraint(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        super(InvalidKeyConstraint, self).__init__()


class InvalidArgument(Exception):
    def __init__(self, cls_name, field_name):
        self.field_name = field_name
        self.cls_name = cls_name
        super(InvalidArgument, self).__init__()
