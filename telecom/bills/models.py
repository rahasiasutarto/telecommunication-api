from django.db import models
from telecom.bills.managers import BillQuerySet


class BillRecord(models.Model):

    start_record = models.ForeignKey(
        "calls.StartRecord",
        on_delete=models.SET_NULL,
        related_name="bill_start_record",
        null=True,
        blank=True,
    )
    end_record = models.ForeignKey(
        "calls.EndRecord",
        on_delete=models.SET_NULL,
        related_name="bill_end_record",
        null=True,
        blank=True,
    )
    call_price = models.DecimalField(
        "price", max_digits=3, decimal_places=2, default=0.00
    )

    @property
    def call_duration(self):
        tdelta = self.end_record.timestamp - self.start_record.timestamp
        days, seconds = tdelta.days, tdelta.seconds
        hours = ((days * 24) + seconds) // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours}h{minutes}m{seconds}s"

    objects = BillQuerySet.as_manager()

    @classmethod
    def calculate_bill_price(cls, *args, **kwargs):
        total = 0
        call_records = BillRecord.objects.get_bill_records(
            subscriber=kwargs["subscriber"],
            month=kwargs["month"],
            year=kwargs["year"],
        )
        for call in call_records:
            total += call.call_price
        return total

    class Meta:
        verbose_name = "bill"
        verbose_name_plural = "bills"
