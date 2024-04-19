from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="main_index"),
    path("<int:flight_ki_id>", views.flight, name="flight_name"),
    path("<int:flight_ki_id>/book", views.book, name="book_kr")
]