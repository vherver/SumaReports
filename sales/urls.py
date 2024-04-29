from django.urls import path

from sales.views import SalesList, SaleDetailView

urlpatterns = [
    path("", SalesList.as_view(), name="sales"),
    path("<int:pk>/", SaleDetailView.as_view(), name="sale_detail"),

]
