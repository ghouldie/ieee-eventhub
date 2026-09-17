# IEEE EventHub

IEEE EventHub is a simple event management web application developed as part of the IEEE ITB Student Branch 2026 Probation Phase for the Fullstack Developer subdivision.

The application allows visitors to view IEEE events and provides an administrator dashboard for managing event information.

## Features

- Public event list
- Event detail page
- Admin authentication
- Protected admin dashboard
- Create new events
- Edit existing events
- Delete events
- Event status: Upcoming, Ongoing, and Completed
- SQLite database persistence
- Form validation
- Responsive interface using Bootstrap
- Loading states during form submission
- Empty states when no events are available
- Custom 404 error page

## Tech Stack

### Backend

**Python + Flask**

Flask was chosen because it is lightweight and beginner-friendly while still providing the routing, session management, template rendering, and backend functionality required for this project.

### Frontend

**HTML, Bootstrap, and JavaScript**

HTML is used for page structure, Bootstrap provides responsive styling and reusable interface components, while JavaScript is used for interactions such as loading states and delete confirmation.

### Database

**SQLite**

SQLite was selected because it is simple to configure, requires no separate database server, and is suitable for a small event management application.

### Template Engine

**Jinja2**

Jinja2 is integrated with Flask and is used to dynamically display event data from the backend inside HTML templates.

## Architecture

The application uses a simple server-side rendered architecture.

```text
Browser
   |
   v
Flask Routes
   |
   +----> Jinja2 Templates
   |
   v
SQLite Database
```

Public users can request event information through Flask routes. Flask retrieves the required data from SQLite and renders the result using Jinja2 templates.

Administrators authenticate through the login page. After authentication, Flask stores the admin session and allows access to protected event management routes.

## Project Structure

```text
ieee-eventhub/
|
|-- app.py
|-- init_db.py
|-- add_admin.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
|
|-- static/
|   `-- js/
|       `-- loading.js
|
`-- templates/
    |-- index.html
    |-- event_detail.html
    |-- admin_login.html
    |-- admin_dashboard.html
    |-- create_event.html
    |-- edit_event.html
    `-- 404.html
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/ghouldie/ieee-eventhub.git
cd ieee-eventhub
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` into a new file named `.env`.

Example:

```env
SECRET_KEY=your-own-secret-key
```

The `.env` file is ignored by Git and should not be committed to the repository.

### 5. Initialize the database

```bash
python init_db.py
```

This creates the `events` table and adds sample events when the database is empty.

### 6. Create the demo administrator

```bash
python add_admin.py
```

This creates the administrator account required to access the admin dashboard.

### 7. Run the application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Demo Admin Account

```text
Username: admin
Password: ieee123
```

The password is stored in the SQLite database as a generated password hash rather than plain text.

## Main Routes

```text
/                         Public event list
/event/<event_id>          Event detail
/admin/login               Administrator login
/admin/dashboard           Administrator dashboard
/admin/event/create        Create event
/admin/event/<id>/edit     Edit event
/admin/event/<id>/delete   Delete event
/admin/logout              Logout
```

## Validation and Error Handling

The application performs basic server-side validation when creating or editing an event. Required fields cannot be empty, and event status must use one of the supported values.

A custom 404 page is displayed when a requested event or page cannot be found.

The interface also provides empty states and loading feedback for relevant actions.

## Known Limitations

This project was designed as a small probation-phase web application rather than a production deployment.

The current implementation uses local SQLite storage and basic session-based authentication. Advanced functionality such as CSRF protection, role-based access control, password reset, image upload, search, filtering, pagination, and production deployment configuration is not currently implemented.

Flask debug mode is intended only for local development.

## AI Usage

AI assistance, primarily ChatGPT, was used during development as a learning and debugging tool.

AI was used to help explain Flask concepts, review implementation ideas, identify errors, suggest project structure, and assist with documentation. The implementation was tested and reviewed during development, and responsibility for the submitted project remains with the developer.

## Developer

**Muchsin Bin Edo Assaidi**

IEEE ITB Student Branch 2026 Probation Phase  
Fullstack Developer