# Order Service

The **Order Service** is a microservice responsible for managing orders in a restaurant. 
It handles the entire lifecycle of an order, from creation to fulfillment, including updating, 
canceling, and tracking orders. This service is built using **FastAPI**, **SQLModel**, and **Docker**, 
and uses **Poetry** for dependency management.


---

## Features
- Create new orders.
- Retrieve order details.
- Update order status (e.g., `pending`, `preparing`, `ready`, `delivered`).
- Add or remove items from an order.
- Cancel an order.
- Built with FastAPI for high performance and easy API development.
- Uses SQLModel for database management and ORM functionality.
- Dockerized for easy deployment and scalability.

---

## Technologies Used
- **Python**: Programming language.
- **FastAPI**: Web framework for building APIs.
- **SQLModel**: ORM for database management.
- **SQLite**: Lightweight database for development.
- **Docker**: Containerization for deployment.
- **Uvicorn**: ASGI server for running FastAPI.
- **Poetry**: Dependency management and packaging.

---

## Setup and Installation

### Prerequisites
- Python 3.9 or higher.
- Docker (optional, for containerization).
- Poetry installed. If not, install it using:
  ```bash
  pip install poetry
