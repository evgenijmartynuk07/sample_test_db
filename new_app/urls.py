from django.urls import path
from .views import TickerViewSet


urlpatterns = [
    path(
        "tickers/",
        TickerViewSet.as_view({"get": "list"}),
        name="tickers-list",
    ),
]


app_name = "new_app"
