
from django.urls import path
from booking_v2.views import SignupRegisterview
from booking_v2.views import AppointmentListCreateview,AppointmentRetrieveUpdateDeleteView
urlpatterns=[
    path('signup/',SignupRegisterview.as_view()),

    path('appointement/',AppointmentListCreateview.as_view()),

    path('appointment/<int:pk>/',AppointmentRetrieveUpdateDeleteView.as_view()),
]