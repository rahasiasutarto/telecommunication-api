from django.apps import AppConfig


class CallsConfig(AppConfig):
    name = "telecom.calls"
    verbose_name = "Call detail records"

    def ready(self):
        import telecom.calls.signals  # noqa
