from .models import Product

from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
            'active': ['exact']
        }