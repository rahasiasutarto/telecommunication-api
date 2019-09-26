import pytest

from datetime import datetime
from model_mommy import mommy
from telecom.calls.models import EndRecord, StartRecord
from telecom.calls.serializers import EndRecordSerializer, StartRecordSerializer

pytestmark = pytest.mark.django_db


def test_required_fields():
    fields = ["call_id", "type", "timestamp"]
    start_serializer = StartRecordSerializer(data={})
    end_serializer = EndRecordSerializer(data={})

    assert False == start_serializer.is_valid()
    assert len(fields) == len(start_serializer.errors)

    assert False == end_serializer.is_valid()
    assert len(fields) == len(end_serializer.errors)


def test_create_valid_start_record():
    start_record = {
        "call_id": 1,
        "type": "start",
        "timestamp": datetime.now(),
        "source": "61982027277",
        "destination": "61988774456",
    }
    serializer = StartRecordSerializer(data=start_record)
    assert True == serializer.is_valid()


def test_create_valid_end_record():
    end_record = {
        "call_id": 1,
        "type": EndRecord.END_RECORD,
        "timestamp": datetime.now(),
    }
    serializer = EndRecordSerializer(data=end_record)
    assert True == serializer.is_valid()


def test_create_invalid_start_record():
    serializer = StartRecordSerializer(data=None)
    assert False == serializer.is_valid()


def test_create_invalid_end_record():
    serializer = EndRecordSerializer(data=None)
    assert False == serializer.is_valid()
