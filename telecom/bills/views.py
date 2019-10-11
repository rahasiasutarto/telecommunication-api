from datetime import datetime, timedelta

from rest_framework import status, viewsets
from rest_framework.response import Response
from telecom.bills.models import BillRecord
from telecom.bills.serializers import BillRecordSerializer


class BillRecordViewSet(viewsets.ViewSet):
    """
    List bill records from specific phone
    """

    def list(self, request, subscriber=None):
        today = datetime.today()
        last_period = today.replace(day=1) - timedelta(days=1)

        month = request.query_params.get("month", str(last_period.month))
        year = request.query_params.get("year", str(last_period.year))

        search_data = dict(subscriber=subscriber, month=month, year=year)

        queryset = BillRecord.objects.get_bill_records(**search_data)
        serializer = BillRecordSerializer(queryset, many=True)
        resp_data = dict(
            subscriber=subscriber,
            bill_price=BillRecord.calculate_bill_price(**search_data),
            month=month,
            year=year,
            call_detail=serializer.data,
        )
        return Response(resp_data, status=status.HTTP_200_OK)


bills_list = BillRecordViewSet.as_view({"get": "list"})
