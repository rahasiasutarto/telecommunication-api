import json
from datetime import datetime

import pytest
from django.shortcuts import resolve_url
from model_mommy import mommy
from rest_framework import status
from telecom.calls.models import EndRecord, StartRecord
from telecom.calls.utils import timestamp_converter

pytestmark = pytest.mark.django_db


@pytest.fixture
def start_list_url():
    return resolve_url("calls:start-list")


def test_start_list_status_code(client, start_list_url):
    response = client.get(start_list_url)
    assert response.status_code == status.HTTP_200_OK


def test_create_valid_start_record(client, start_list_url):
    payload = dict(
        call_id=1,
        type=StartRecord.START_RECORD,
        timestamp=datetime.now(),
        source="61982037480",
        destination="62984570900",
    )
    response = client.post(
        start_list_url,
        data=json.dumps(payload, default=timestamp_converter),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_create_invalid_start_record(client, start_list_url):
    response = client.post(
        start_list_url, data=json.dumps(None), content_type="application/json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def start_detail_url():
    valid_obj = mommy.make(
        StartRecord,
        type="start",
        source="61982027370",
        destination="61983746578",
    )
    return resolve_url("calls:start-detail", pk=valid_obj.pk)


def test_update_valid_start_record(client, start_detail_url):
    payload = dict(
        call_id=2,
        type="start",
        timestamp=datetime.now(),
        source="61982037481",
        destination="62984570910",
    )
    response = client.put(
        start_detail_url,
        data=json.dumps(payload, default=timestamp_converter),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK


def test_delete_valid_start_record(client, start_detail_url):
    response = client.delete(start_detail_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_update_invalid_start_record(client, start_detail_url):
    response = client.put(
        start_detail_url, data=json.dumps(None), content_type="application/json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_invalid_start_record(client, start_detail_url):
    response = client.delete(resolve_url("calls:start-detail", pk=None))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.fixture
def end_list_url():
    return resolve_url("calls:end-list")


def test_end_list_status_code(client, end_list_url):
    response = client.get(end_list_url)
    assert response.status_code == status.HTTP_200_OK


def test_create_valid_end_record(client, end_list_url):
    payload = dict(
        call_id=3, type=EndRecord.END_RECORD, timestamp=datetime.now()
    )
    response = client.post(
        end_list_url,
        data=json.dumps(payload, default=timestamp_converter),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_create_invalid_end_record(client, end_list_url):
    response = client.post(
        end_list_url, data=json.dumps(None), content_type="application/json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def end_detail_url():
    valid_obj = mommy.make(
        EndRecord, type=EndRecord.END_RECORD, source=None, destination=None
    )
    return resolve_url("calls:end-detail", pk=valid_obj.pk)


def test_update_valid_end_record(client, end_detail_url):
    payload = dict(
        call_id=4, type=EndRecord.END_RECORD, timestamp=datetime.now()
    )
    response = client.put(
        end_detail_url,
        data=json.dumps(payload, default=timestamp_converter),
        content_type="application/json",
    )
    assert response.status_code == status.HTTP_200_OK


def test_delete_valid_end_record(client, end_detail_url):
    response = client.delete(end_detail_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_update_invalid_end_record(client, end_detail_url):
    response = client.put(
        end_detail_url, data=json.dumps(None), content_type="application/json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_invalid_end_record(client, end_detail_url):
    response = client.delete(resolve_url("calls:end-detail", pk=None))
    assert response.status_code == status.HTTP_404_NOT_FOUND
