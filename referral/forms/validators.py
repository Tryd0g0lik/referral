from cfgv import ValidationError
from email_validator import EmailNotValidError, validate_email


def validate_emails(email) -> [str, bool]:
    """
    This is a email's validator.
    :param email: str. Min. Length is 7 symbols.
    :return: str if is all Ok and False if what wrong.
    """
    if len(email.data) < 7:
        raise ValidationError("We're sorry! Your email has less than the 7 symbols.")
    try:
        emailinfo = validate_email(email.data, check_deliverability=False)
        email = emailinfo.normalized
        return email
    except EmailNotValidError as err:
        print(f"This is an email not a valid: {str(err)}")
        return False
