from django.core.management.base import BaseCommand
from mainapp.models import Product
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(
            Q(category__name='Обувь') | Q(id=4))    # или

        # products = Product.objects.filter(
        #     Q(category__name='Обувь') & Q(id=4))  # и

        # products = Product.objects.filter(
        #     ~Q(category__name='Обувь'))           # не

        # products = Product.objects.filter(
        #     ~Q(category__name='Обувь'), id=4)           # не и равно
        print(products)
