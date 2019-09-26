from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from telecom.calls.managers import EndManager, StartManager
from telecom.calls.validators import phone_validator


class CallRecord(models.Model):
    START_RECORD = "start"
    END_RECORD = "end"

    RECORD_TYPE = ((START_RECORD, "Start"), (END_RECORD, "End"))

    call_id = models.PositiveIntegerField(
        help_text="Unique for each call record pair"
    )
    type = models.CharField(
        max_length=5,
        choices=RECORD_TYPE,
        help_text="Its a call start or end record",
    )
    timestamp = models.DateTimeField(
        "timestamp", help_text="The timestamp of when the event occured"
    )
    source = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        help_text="The subscriber phone number that originated call",
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(11),
            phone_validator,
        ],
    )
    destination = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        help_text="The phone number receiving the call",
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(11),
            phone_validator,
        ],
    )

    created_at = models.DateTimeField("created at", auto_now_add=True)

    class Meta:
        verbose_name = "call"
        verbose_name_plural = "calls"
        unique_together = ("call_id", "type")
        ordering = ("-type", "-timestamp")

    def __str__(self):
        return f"Call {self.type} #{self.call_id}"


class StartRecord(CallRecord):
    objects = StartManager()

    class Meta:
        proxy = True


class EndRecord(CallRecord):
    objects = EndManager()

    class Meta:
        proxy = True
