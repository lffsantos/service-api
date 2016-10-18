from decouple import config
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config('SECRET_KEY'))
    return serializer.dumps(email, salt=config('SECURITY_PASSWORD_SALT'))


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config('SECRET_KEY'))
    try:
        email = serializer.loads(
            token,
            salt=config('SECURITY_PASSWORD_SALT'),
            max_age=expiration
        )
    except:
        return False
    return email


def send_email(to, subject, template):
    from service import mail
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=config('MAIL_DEFAULT_SENDER')
    )
    # TRiCK TO PASS ON TRAVIS
    if not config('DEBUG'):
        mail.send(msg)
