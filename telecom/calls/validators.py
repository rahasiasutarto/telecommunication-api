from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r"^[0-9]*$", message="Only numbers are allowed."
)
