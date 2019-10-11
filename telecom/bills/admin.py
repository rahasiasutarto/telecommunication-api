from django.contrib import admin
from telecom.bills.models import BillRecord


class BillRecordAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "subscriber",
        "destination",
        "call_duration",
        "call_price",
    ]
    list_filter = (
        "start_record__source",
        "start_record__destination",
        "call_price",
    )

    def subscriber(self, obj):
        return obj.start_record.source

    subscriber.short_description = "source"

    def destination(self, obj):
        return obj.start_record.destination

    destination.short_description = "destination"


admin.site.register(BillRecord, BillRecordAdmin)
