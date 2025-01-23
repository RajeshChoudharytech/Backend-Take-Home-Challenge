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
   git clone <repository-url>
   cd project_root
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

## Docker Details

### `docker-compose.yml`

```yaml
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    command: >
      sh -c "python manage.py migrate && \
             python manage.py collectstatic --noinput && \
             gunicorn config.wsgi:application --bind 0.0.0.0:8000"
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      DJANGO_SETTINGS_MODULE: ecommerce.settings
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"

  tests:
    build:
      context: .
      dockerfile: Dockerfile
    command: pytest --cov=.
    volumes:
      - .:/app
    environment:
      DJANGO_SETTINGS_MODULE: ecommerce.settings
    depends_on:
      - db
```

---

## Notes

- Ensure your `media/` directory is writable for image uploads.
- Update the `DJANGO_SETTINGS_MODULE` in the `docker-compose.yml` file if your project name differs.
- Adjust the `POSTGRES_*` environment variables in `docker-compose.yml` to match your setup.

