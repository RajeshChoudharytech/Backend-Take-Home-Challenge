# E-Commerce REST API

This project is a production-grade RESTful API for a simple e-commerce platform. The API allows users to view available products, add new products, and place orders. The application includes proper exception handling, test cases using pytest, and Docker support for containerized deployment.

## Features

- **Product Management**: 
  - Retrieve a list of products
  - Add new products with name, description, price, stock, and image

- **Order Management**:
  - Place orders for selected products
  - Validate stock before confirming orders
  - Deduct stock on successful orders

- **Test Coverage**:
  - Comprehensive test cases written using pytest and pytest-django

- **Dockerized Deployment**:
  - Easily run the application and tests in a containerized environment

---

## Folder Structure

```
project_root/
|
├── e_commerce_platform/
        ├── api/ 
            ├── models.py           
            ├── serializers.py      
            ├── views.py            
            └── urls.py
        ├── tests/                  
            ├── test_api.py
│
│
├── Dockerfile              
├── docker-compose.yml      
├── manage.py               
├── pytest.ini             
├── requirements.txt        
└── README.md               
```

---

## Prerequisites

- Docker and Docker Compose installed on your system
- Python 3.9+ (optional for local development)

---

## Setup Instructions

### Using Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RajeshChoudharytech/Backend-Take-Home-Challenge.git
   cd Backend-Take-Home-Challenge
   ```

2. **Build the Docker image**:
   ```bash
   docker-compose build
   ```

3. **Run the application**:
   ```bash
   docker-compose up
   ```

4. **Access the application**:
   - API base URL: `http://localhost:8000`

5. **Run the tests**:
   ```bash
   docker-compose run tests
   ```

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Run the tests**:
   ```bash
   pytest --cov=.
   ```

---

## API Endpoints

### Products
- **GET /products/**: Retrieve a list of all products.
- **POST /products/create/**: Add a new product.
  ```json
  {
      "name": "Product Name",
      "description": "Product Description",
      "price": 10.99,
      "stock": 100,
      "image": "image_url"
  }
  ```

### Orders
- **POST /orders/create/**: Place a new order.
  ```json
  {
      "items": [
          {"product_id": 1, "quantity": 2},
          {"product_id": 2, "quantity": 1}
      ]
  }
  ```

---

## Running Tests

### Using Docker:
```bash
docker-compose run tests
```

### Locally:
```bash
pytest --cov=.
```

---