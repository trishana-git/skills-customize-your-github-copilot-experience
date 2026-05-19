# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You'll create a web service with multiple endpoints, request/response handling, and data validation. By completing this assignment, you'll understand how to design RESTful services, handle HTTP methods, and structure API code professionally.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description
Build a REST API for managing a list of todos using FastAPI. The API should support creating, reading, updating, and deleting todo items. Implement proper HTTP methods and status codes for each operation.

#### Requirements
Completed API should:

- Define a data model for todo items (id, title, description, completed status)
- Implement GET endpoint to retrieve all todos
- Implement GET endpoint to retrieve a specific todo by id
- Implement POST endpoint to create a new todo
- Implement PUT endpoint to update an existing todo
- Implement DELETE endpoint to remove a todo
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include basic request validation for input data

### 🛠️ Add Query Parameters and Filtering

#### Description
Enhance the API by adding query parameters to filter and search through todos. Implement optional filtering, sorting, and pagination features to make the API more powerful.

#### Requirements
Completed API should:

- Accept query parameters for filtering (e.g., by completion status)
- Support searching todos by title or description
- Implement basic pagination (limit and offset parameters)
- Return filtered results correctly based on query parameters
