from django.db.models.signals import post_save
from django.dispatch import receiver
from telecom.bills.models import BillRecord
from telecom.calls.models import EndRecord, StartRecord


@receiver(post_save, sender=StartRecord)
def start_record_validation(sender, instance, created, **kwargs):
    if created:
        record = EndRecord.objects.filter(call_id=instance.call_id).first()
        if record:
            create_bill_record(start=instance, end=record)


@receiver(post_save, sender=EndRecord)
def end_record_validation(sender, instance, created, **kwargs):
    if created:
        record = StartRecord.objects.filter(call_id=instance.call_id).first()
        if record:
            create_bill_record(start=record, end=instance)


def create_bill_record(start, end):
    BillRecord.objects.create(
        start_record=start, end_record=end, call_price=5.00
    )
