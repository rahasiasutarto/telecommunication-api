from django.urls import path, register_converter
from telecom.bills import converters, views

app_name = "bills"

register_converter(converters.PhoneNumberConverter, "phone")

urlpatterns = [path("<phone:subscriber>/", views.bills_list, name="bill-list")]
