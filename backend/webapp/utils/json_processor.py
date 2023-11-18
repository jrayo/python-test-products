import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def process_products(file_path):
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
    except (IOError, ValueError):
        return [], 0

    three_months_ago = datetime.now() - relativedelta(months=3)
    recent_products = [
        p for p in products
        if 'updated_at' in p and 'price' in p and 'rating'
        in p and datetime.fromisoformat(p['updated_at']) > three_months_ago
    ]

    sorted_products = sorted(recent_products, key=lambda p: p['price'], reverse=True)

    top_10_products = sorted_products[:10]

    if not top_10_products:
        return [], 0

    average_rating = sum(p['rating'] for p in top_10_products) / len(top_10_products)
    average_rating = round(average_rating, 2)

    return top_10_products, average_rating


def load_all_products(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
