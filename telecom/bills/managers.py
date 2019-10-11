from django.db import models


class BillQuerySet(models.QuerySet):
    def get_bill_records(self, *args, **kwargs):
        return self.filter(
            end_record__timestamp__month=kwargs["month"],
            end_record__timestamp__year=kwargs["year"],
            end_record__call_id__in=self.filter(
                start_record__source=kwargs["subscriber"]
            ).values_list("start_record__call_id", flat=True),
        )
