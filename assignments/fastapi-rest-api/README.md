# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a REST API using the FastAPI framework to practice endpoint design, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Define API Models and CRUD Endpoints

#### Description
Create a FastAPI application with Pydantic models and CRUD endpoints for managing item data in memory.

#### Requirements
Completed program should:

- Define a Pydantic model for `Item` with `id`, `name`, `description`, `price`, and optional `tax`.
- Implement endpoints to create, read, update, and delete items.
- Validate incoming JSON request bodies using Pydantic models.
- Return JSON responses and appropriate HTTP status codes for each operation.

### 🛠️ Add Query Parameters and API Documentation

#### Description
Enhance the API with query parameters for searching or limiting results and use FastAPI's automatic documentation.

#### Requirements
Completed program should:

- Support optional query parameters such as `q` to search item names or descriptions and `limit` to control result size.
- Filter or limit returned items based on query values.
- Allow students to explore the API documentation at `/docs`.
- Keep the API implementation clear and easy to extend.
