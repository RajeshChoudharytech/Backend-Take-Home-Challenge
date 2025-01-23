import pytest
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Product

# Fixtures
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_products(db):
    """Fixture to create a list of products."""
    products = [
        Product.objects.create(
            name="Wireless Headphones",
            description="Noise-cancelling wireless headphones with Bluetooth connectivity.",
            price=99.99,
            stock=144,
        ),
        Product.objects.create(
            name="Smartphone",
            description="Latest model with 128GB storage and 6GB RAM.",
            price=599.99,
            stock=198,
        ),
        Product.objects.create(
            name="Laptop",
            description="14-inch laptop with Intel i7 processor and 16GB RAM.",
            price=999.99,
            stock=47,
        ),
        Product.objects.create(
            name="Electric Kettle",
            description="1.5L electric kettle with automatic shut-off feature.",
            price=29.99,
            stock=294,
        ),
        Product.objects.create(
            name="Bluetooth Speaker",
            description="Portable Bluetooth speaker with high-quality sound and waterproof design.",
            price=49.99,
            stock=120,
        ),
    ]
    return products

@pytest.fixture
def create_sample_products(db):
    """Fixture to create a smaller set of sample products."""
    product1 = Product.objects.create(
        name="Wireless Headphones",
        description="Noise-cancelling wireless headphones with Bluetooth connectivity.",
        price=99.99,
        stock=144,
    )
    product2 = Product.objects.create(
        name="Smartphone",
        description="Latest model with 128GB storage and 6GB RAM.",
        price=599.99,
        stock=198,
    )
    return product1, product2

# Tests
@pytest.mark.django_db
def test_get_product_list(api_client, create_products):
    """Test retrieving product list"""
    response = api_client.get("/products/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5

@pytest.mark.django_db
def test_create_order_success(api_client, create_sample_products):
    """Test successful order placement"""
    product1, product2 = create_sample_products
    data = {
        "items": [
            {"product_id": product1.id, "quantity": 2},
            {"product_id": product2.id, "quantity": 1},
        ]
    }
    response = api_client.post("/orders/create/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "total_price" in response.data
    assert response.data["total_price"] == pytest.approx((2 * 99.99) + (1 * 599.99))

    # Check if stock is deducted correctly
    product1.refresh_from_db()
    product2.refresh_from_db()
    assert product1.stock == 142
    assert product2.stock == 197

@pytest.mark.django_db
def test_create_order_insufficient_stock(api_client, create_sample_products):
    """Test order creation failure due to insufficient stock"""
    product1, _ = create_sample_products
    data = {
        "items": [
            {"product_id": product1.id, "quantity": 200},  # More than available stock
        ]
    }
    response = api_client.post("/orders/create/", data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Insufficient stock" in str(response.data)
