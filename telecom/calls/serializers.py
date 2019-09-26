from rest_framework import serializers
from telecom.calls.models import CallRecord, EndRecord, StartRecord


class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = "__all__"


class StartRecordSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = StartRecord
        fields = ["id", "call_id", "type", "timestamp", "source", "destination"]

    def validate(self, data):
        if "start" not in data["type"]:
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

    def validate(self, data):
        if "end" not in data["type"]:
            raise serializers.ValidationError("The type of call must be start.")

        return data
