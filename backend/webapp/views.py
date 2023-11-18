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
    content = """
        <html>
            <head>
                <title>Product API Home</title>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        text-align: center; 
                        margin-top: 3em;
                        background-color: #f5f5f5
                    }
                    h1 { 
                        color: #333; 
                    }
                    ul { 
                        padding: 0; 
                    }
                    li { 
                        margin: 10px 0; 
                    }
                    a { 
                        text-decoration: none; 
                        color: darkblue; 
                    }
                    a:hover { 
                        color: blue; 
                    }
                    p, ul {
                        text-align: left;
                        margin: 2em;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Product API Home Page</h1>
                <p>Use the following links to access the API endpoints:</p>
                <ul>
                    <li><a href="/api/products">All Products API</a></li>
                    <li><a href="/api/products/top-rated">Top Rated Products API</a></li>
                </ul>
            </body>
        </html>
    """
    return HttpResponse(content)
