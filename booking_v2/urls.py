
from django.urls import path
from booking_v2.views import SignupRegisterview
from booking_v2.views import TurfBokingRetrieveUpdateDeleteView,TurfBookingListCreateView,AppointmentListCreateview
urlpatterns=[
    path('signup/',SignupRegisterview.as_view()),

    path('booking/',TurfBookingListCreateView.as_view()),
    path('booking/<int:pk>/',TurfBokingRetrieveUpdateDeleteView.as_view()),

    path('appointement/',AppointmentListCreateview.as_view()),
]