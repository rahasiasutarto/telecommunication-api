import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from model_mommy import mommy
from telecom.calls.managers import EndManager, StartManager
from telecom.calls.models import EndRecord, StartRecord

pytestmark = pytest.mark.django_db


@pytest.fixture
def start_call():
    return StartRecord.objects.create(
        call_id=1,
        type=StartRecord.START_RECORD,
        timestamp=timezone.now(),
        source="61997460291",
        destination="62984762097",
    )


@pytest.fixture
def end_call():
    return EndRecord.objects.create(
        call_id=1, type=EndRecord.END_RECORD, timestamp=timezone.now()
    )


def test_create_call_records(start_call, end_call):
    assert (
        StartRecord.objects.exists() is True
        and EndRecord.objects.exists() is True
    )


def test_str(start_call, end_call):
    assert f"Call {start_call.type} #{start_call.call_id}" == str(start_call)
    assert f"Call {end_call.type} #{end_call.call_id}" == str(end_call)


def test_start_manager():
    assert isinstance(StartRecord.objects, StartManager)
    assert isinstance(EndRecord.objects, EndManager)


def test_unique_together(start_call, end_call):
    with pytest.raises(IntegrityError):
        mommy.make(StartRecord, call_id=1, type=StartRecord.START_RECORD)
        mommy.make(EndRecord, call_id=1, type=EndRecord.END_RECORD)


@pytest.mark.parametrize("kind", ["invalid", "null"])
def test_type_invalid_choice(kind):
    start_call = mommy.make(StartRecord, type=kind)
    end_call = mommy.make(EndRecord, type=kind)
    pytest.raises(ValidationError, start_call.full_clean)
    pytest.raises(ValidationError, end_call.full_clean)


@pytest.mark.parametrize("number", ["123", "123456789012", "A1234B", "AABBBB"])
def test_invalid_phone_number(number):
    call = mommy.make(
        StartRecord,
        type=StartRecord.START_RECORD,
        source=number,
        destination=number,
    )
    pytest.raises(ValidationError, call.full_clean)


@pytest.mark.parametrize("field_name", ["source", "destination"])
def test_fields_can_be_blank_or_null(field_name):
    field = EndRecord._meta.get_field(field_name)
    assert field.blank is True and field.null is True
