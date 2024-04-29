from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import generics
from .models import Sale
from .serializers import SalesSerializer

class SalesList(generics.ListAPIView):
    serializer_class = SalesSerializer
    queryset = Sale.objects.all().order_by("-id")

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        if start_date and end_date:
            self.queryset = self.queryset.filter(date__range=[start_date, end_date])
        return render(request, 'sales_list.html', {'sales':
                                                       self.get_queryset()})


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sale_detail.html'
    context_object_name = 'sale'