from rest_framework.views import APIView
from rest_framework.response import Response
from backend.webapp.utils.json_processor import load_all_products, process_products
from django.http import HttpResponse


class AllProductsAPIView(APIView):
    def get(self, request, format=None):
        file_path = 'backend/data/products.json'
        products = load_all_products(file_path)
        return Response(products)


class TopRatedAPIView(APIView):
    def get(self, request, format=None):
        file_path = 'backend/data/products.json'
        top_products, avg_rating = process_products(file_path)
        data = {
            'top_10_products': top_products,
            'average_rating': avg_rating
        }
        return Response(data)


def home_view(request):
    return HttpResponse("Welcome to the Home Page")
