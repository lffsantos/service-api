from service import api_v1
from service.members import exceptions as exc


@api_v1.errorhandler(exc.AuxModelNotFound)
def handle_auxmodel_not_found(error):
    msg = {
        'error': '{}NotFound'.format(error.cls_name),
        'field_key': error.key,
        'field_value': error.value
    }
    return msg, 404


@api_v1.errorhandler(exc.AuxModelAlreadyExists)
def handle_auxmodel_already_exist(error):
    msg = {
        'error': '{}AlreadyExists'.format(error.cls_name),
        'field_key': error.key,
        'field_value': error.value
    }
    return msg, 409


@api_v1.errorhandler(exc.MemberNotFound)
def handle_member_not_found(error):
    msg = {
        'error': 'MemberNotFound',
        'email': error.email
    }
    return msg, 404


@api_v1.errorhandler(exc.MemberAlreadyExists)
def handle_member_already_exist(error):
    msg = {
        'error': 'MemberAlreadyExists',
        'field_key': error.key,
        'field_value': error.value
    }
    return msg, 409


@api_v1.errorhandler(exc.InvalidValueError)
def handle_invalid_value_error(error):
    msg = {
        'error': 'InvalidValueError',
        'field_name': error.field_name,
        'field_value': error.field_value
    }
    return msg, 400


@api_v1.errorhandler(exc.MemberAlreadyExists)
def handle_invalid_constraint(error):
    msg = {
        'error': 'InvalidConstraint',
        'field_key': error.key,
        'field_value': error.value
    }
    return msg, 400


@api_v1.errorhandler(exc.InvalidArgument)
def handle_invalid_argument(error):
    msg = {
        'error': 'InvalidValueArgument',
        'field_name': error.field_name
    }
    return msg, 400


@api_v1.errorhandler
def default_error_handler(error):
    """Default error handler"""
    return {'message': str('Internal Server Error')}, getattr(error, 'code', 500)
