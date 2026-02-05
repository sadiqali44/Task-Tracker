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

cd backend/tasktracker
python -m venv venv
venv\Scripts\activate      (Windows)
source venv/bin/activate  (macOS/Linux)
pip install -r requirements.txt
python manage.py runserver

Backend URL:
http://127.0.0.1:8000


Frontend Setup

cd frontend
npm install
npm run dev

Frontend URL:
http://localhost:5173


API Endpoints

Base URL:
/api

POST   /tasks/                Create task
GET    /tasks/all/            Get all tasks
PATCH  /tasks/<id>/           Update task status
DELETE /tasks/<id>/delete/    Delete task


Notes
- MongoDB runs locally on mongodb://localhost:27017
- CORS enabled for frontend
- Backend validates task status rules
- AI tools used for guidance and productivity


Conclusion
This project demonstrates basic logic, API design, MongoDB integration,
and frontend–backend data flow as required for the machine test.
