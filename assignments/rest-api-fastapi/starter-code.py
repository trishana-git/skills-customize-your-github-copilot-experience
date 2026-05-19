from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Data Models
class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage (for this assignment)
todos_db: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastAPI", description="Study FastAPI basics", completed=True),
    TodoItem(id=2, title="Build a REST API", description="Create a todo API", completed=False),
]

# TODO: Implement your API endpoints here
# Hints:
# - Use @app.get(), @app.post(), @app.put(), @app.delete() decorators
# - Access path parameters with function arguments: def get_todo(todo_id: int)
# - Use query parameters with Optional types: skip: int = 0, limit: int = 10
# - Return appropriate status codes using status parameter: status_code=201

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
