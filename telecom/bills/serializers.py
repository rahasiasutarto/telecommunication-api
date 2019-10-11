from rest_framework import serializers
from telecom.bills.models import BillRecord


class BillRecordSerializer(serializers.ModelSerializer):
    destination = serializers.SerializerMethodField()
    start_date = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()

    class Meta:
        model = BillRecord
        fields = [
            "destination",
            "start_date",
            "start_time",
            "call_duration",
            "call_price",
        ]

    def get_destination(self, obj):
        return obj.start_record.destination

    def get_start_date(self, obj):
        return obj.start_record.timestamp.date()

    def get_start_time(self, obj):
        return obj.start_record.timestamp.time()
