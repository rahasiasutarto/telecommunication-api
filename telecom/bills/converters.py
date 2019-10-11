class PhoneNumberConverter:
    regex = "[0-9]{10,11}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value
