from rest_framework import serializers
from telecom.calls.models import CallRecord, EndRecord, StartRecord


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = "__all__"


class StartRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartRecord
        fields = ["id", "call_id", "type", "timestamp", "source", "destination"]
        read_only_fields = ["id"]

    def validate(self, data):
        if CallRecord.START_RECORD not in data["type"]:
            raise serializers.ValidationError("The type of call must be start.")

        if data["source"] is None or data["source"] is False:
            raise serializers.ValidationError(
                "A start call must have a source phone number."
            )

        if data["destination"] is None or data["destination"] is False:
            raise serializers.ValidationError(
                "A start call must have a destination phone number."
            )

        return data


class EndRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndRecord
        fields = ["id", "call_id", "type", "timestamp"]
        read_only_fields = ["account_name"]

    def validate(self, data):
        if CallRecord.END_RECORD not in data["type"]:
            raise serializers.ValidationError("The type of call must be end.")

        if data["type"] == CallRecord.END_RECORD and "source" in data:
            raise serializers.ValidationError(
                "A end call must not have a source number."
            )

        if data["type"] == CallRecord.END_RECORD and "destination" in data:
            raise serializers.ValidationError(
                "A end call must not have a destination number."
            )

        return data
