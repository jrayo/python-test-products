import json
from unittest.mock import mock_open, patch
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from freezegun import freeze_time


class ProductAPITestCase(TestCase):
    mock_file_data = json.dumps([
        {
            "name": "Product A",
            "price": 100,
            "rating": 4.5,
            "updated_at": "2023-09-18"
        },
        {
            "name": "Product B",
            "price": 200,
            "rating": 4.2,
            "updated_at": "2023-06-11"
        },
        {
            "name": "Product C",
            "price": 150,
            "rating": 3.9,
            "updated_at": "2022-12-16"
        },
        {
            "name": "Product D",
            "price": 300,
            "rating": 4.8,
            "updated_at": "2023-01-31"
        },
        {
            "name": "Product E",
            "price": 250,
            "rating": 4.0,
            "updated_at": "2023-10-02"
        }
    ])

    def setUp(self):
        self.client = APIClient()

    @patch('builtins.open')
    def test_all_products_api_view(self, mock_file):
        mock_file.return_value = mock_open(read_data=self.mock_file_data).return_value
        url = reverse('products')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        self.assertEqual(len(response_data), 5)

    @patch('builtins.open')
    @freeze_time("2023-11-18")
    def test_top_rated_api_view(self, mock_file):
        mock_file.return_value = mock_open(read_data=self.mock_file_data).return_value

        url = reverse('top-rated')

        response = self.client.get(url)
        response_data = response.json()
        expected_average_rating = 4.25
        expected_data = [
            {
                "name": "Product E",
                "price": 250,
                "rating": 4.0,
                "updated_at": "2023-10-02"
            },
            {
                "name": "Product A",
                "price": 100,
                "rating": 4.5,
                "updated_at": "2023-09-18"
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('top_10_products', response_data)
        self.assertIn('average_rating', response_data)

        self.assertIsInstance(response_data['top_10_products'], list)
        self.assertEqual(len(response_data['top_10_products']), 2)
        self.assertEqual(response_data['average_rating'], expected_average_rating)
        self.assertEqual(response_data['top_10_products'], expected_data)
