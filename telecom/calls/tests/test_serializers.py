from datetime import datetime

import pytest
from telecom.calls.models import EndRecord, StartRecord
from telecom.calls.serializers import EndRecordSerializer, StartRecordSerializer

pytestmark = pytest.mark.django_db


def test_required_fields():
    fields = ["call_id", "type", "timestamp"]
    start_serializer = StartRecordSerializer(data={})
    end_serializer = EndRecordSerializer(data={})

    assert start_serializer.is_valid() is False
    assert len(fields) == len(start_serializer.errors)

    assert end_serializer.is_valid() is False
    assert len(fields) == len(end_serializer.errors)


def test_create_valid_start_record():
    start_record = {
        "call_id": 1,
        "type": StartRecord.START_RECORD,
        "timestamp": datetime.now(),
        "source": "61982027277",
        "destination": "61988774456",
    }
    serializer = StartRecordSerializer(data=start_record)
    assert serializer.is_valid() is True


def test_create_valid_end_record():
    end_record = {
        "call_id": 1,
        "type": EndRecord.END_RECORD,
        "timestamp": datetime.now(),
    }
    serializer = EndRecordSerializer(data=end_record)
    assert serializer.is_valid() is True


def test_create_invalid_start_record():
    serializer = StartRecordSerializer(data=None)
    assert serializer.is_valid() is False


def test_create_invalid_end_record():
    serializer = EndRecordSerializer(data=None)
    assert serializer.is_valid() is False
