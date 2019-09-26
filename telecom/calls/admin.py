from django.contrib import admin
from telecom.calls.models import EndRecord, StartRecord


class StartRecordAdmin(admin.ModelAdmin):
    list_display = ["type", "call_id", "timestamp", "source", "destination"]
    date_hierarchy = "timestamp"
    search_fields = ("source", "destination")
    list_filter = ("timestamp",)


class EndRecordAdmin(admin.ModelAdmin):
    list_display = ["type", "call_id", "timestamp"]
    date_hierarchy = "timestamp"
    list_filter = ("timestamp",)


admin.site.register(StartRecord, StartRecordAdmin)
admin.site.register(EndRecord, EndRecordAdmin)
