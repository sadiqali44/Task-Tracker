Task Tracker – Machine Test

Simple Task Tracker built using React, Django REST Framework, and MongoDB.


Tech Stack
- Frontend: React (Vite)
- Backend: Django + Django REST Framework
- Database: MongoDB (PyMongo)


Features
- Create task
- View all tasks
- Update task status (TODO → IN_PROGRESS → DONE)
- Prevent invalid transition (TODO → DONE)
- Delete task (bonus)


Backend Setup

- cd backend/tasktracker
- python -m venv venv
- venv\Scripts\activate      (Windows)
- source venv/bin/activate  (macOS/Linux)
- pip install -r requirements.txt
- python manage.py runserver

Backend URL:
http://127.0.0.1:8000


Frontend Setup

- cd frontend
- npm install
- npm run dev

Frontend URL:
http://localhost:5173


API Endpoints

Base URL:
/api

- POST    /tasks/                Create task
- GET     /tasks/all/            Get all tasks
- PATCH   /tasks/<id>/           Update task status
- DELETE  /tasks/<id>/delete/    Delete task


Notes
- MongoDB runs locally on mongodb://localhost:27017
- CORS enabled for frontend
- Backend validates task status rules
- AI tools used for guidance and productivity


PART 1: Data Model
- Each task contains id, title, status, and createdAt fields.
- Status values are restricted to TODO, IN_PROGRESS, and DONE.
- Fixed status values ensure data consistency and valid task flow.


PART 2: Backend API
- Create Task: Creates a new task with default status TODO.
- Get Tasks: Retrieves all tasks from MongoDB.
- Update Task Status: Updates task status with validation rules.
- Delete Task: Deletes a task by ID (bonus feature).
- Backend returns appropriate error responses for invalid data.


PART 3: UI and Data Flow
- UI is split into TaskList, TaskItem, and TaskForm components.
- Frontend communicates with backend using fetch API.
- State updates trigger UI re-render for real-time updates.
- Component-based structure improves maintainability.


PART 4: Task Status Rule
- Direct transition from TODO to DONE is restricted.
- This rule is enforced in the backend to ensure data integrity.


PART 5: AI Usage
- AI tools were used for guidance and productivity.
- Assisted with API structure, UI refinement, and debugging.
- All logic was manually reviewed and verified.


Conclusion
This project demonstrates basic logic, API design, MongoDB integration,
and frontend–backend data flow as required for the machine test.
