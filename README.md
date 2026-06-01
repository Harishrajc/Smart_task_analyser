# Smart Task Analyser

A simple full-stack task analysis application with a FastAPI backend and a Svelte frontend.

## Project structure

- `backend/` - Python FastAPI service
  - `app/main.py` - application entry point
  - `app/routes.py` - API routes
  - `app/models.py` - database models
  - `app/schemas.py` - request/response schemas
  - `app/database.py` - database connection setup
  - `requirements.txt` - Python dependencies

- `frontend/` - Svelte + Vite web application
  - `src/App.svelte` - main application
  - `src/main.js` - frontend bootstrap
  - `src/lib/api.js` - API helper
  - `package.json` - node dependencies and scripts

- `docker-compose.yml` - development containers for backend and frontend

## Dependencies

### Backend

Install the Python dependencies in a virtual environment:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Dependencies:
- `fastapi`
- `uvicorn`
- `sqlalchemy`

### Frontend

Install the Node dependencies:

```bash
cd frontend
npm install
```

Dependencies:
- `svelte`
- `vite`
- `@sveltejs/vite-plugin-svelte`
- `axios`

## Running the project

### Option 1: Run with Docker Compose

From the repository root:

```bash
docker-compose up --build
```

This will start:
- Backend at `http://localhost:8000`
- Frontend at `http://localhost:5173`

### Option 2: Run manually

#### Start backend

```bash
cd backend
.venv\Scripts\activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Start frontend

```bash
cd frontend
npm run dev
```

Open `http://localhost:5173` in your browser.

## Notes

- The frontend depends on the backend API, so start the backend before the frontend if running manually.
- Use `docker-compose down` to stop the containers.
