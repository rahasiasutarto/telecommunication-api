from rest_framework import viewsets
from telecom.calls.models import CallRecord, EndRecord, StartRecord
from telecom.calls.serializers import (
    CallRecordSerializer,
    EndRecordSerializer,
    StartRecordSerializer,
)


class CallRecordsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List all start and end records.
    """

    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer


class StartRecordViewSet(viewsets.ModelViewSet):
    """
    List all start records, or create a new start record.
    """

    queryset = StartRecord.objects.all()
    serializer_class = StartRecordSerializer


class EndRecordViewSet(viewsets.ModelViewSet):
    """
    List all end records, or create a new end record.
    """

    queryset = EndRecord.objects.all()
    serializer_class = EndRecordSerializer
