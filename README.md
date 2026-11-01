
# Gym Management System

This README provides an overview of the structure and features of a Django application for managing a gym's members, fees and attendance.



## Overview
Developed a Django web application that replaces a gym's paper registers. Staff sign in to register members, keep their personal, fee and trainer details up to date, search the member list, record daily attendance and view a monthly attendance report for each member.



## Technologies Used
* **Django** - Web framework
* **SQLite** - Database
* **Django Forms** - Member and attendance forms with validation
* **HTML, CSS** - Front-end templates

## Features
* **Staff Authentication**: Staff register, log in and log out.
* **Member Management**: Add, view, update and delete members with CNIC, date of birth, contact details, occupation, gender, blood group, height, weight and timings.
* **Fees and Trainers**: Track the admission fee, monthly fee, assigned trainer and trainer fee for each member.
* **Search**: Find members by name.
* **Pagination**: The member list on the home page is split into pages.
* **Attendance**: Record daily attendance for any member.
* **Monthly Attendance Report**: See each member's attendance for the current month.

## Files
* **`gym_django/gym_management_system/`**: Membership and attendance models, forms, views and templates.
* **`gym_django/members/`**: Staff login, logout and registration.
* **`gym_django/templates/base.html`**: Base template shared by all pages.

## How to use
1. **Clone the repository**: Clone the project repository to your local machine.
    ```bash
    git clone https://github.com/Sharjeel-Rauf/Gym_Management_System_Django.git
    cd Gym_Management_System_Django
    ```
2. **Set up a virtual environment**: Create a virtual environment and activate it.
    ```bash
    python -m venv venv
    venv\Scripts\activate        # Windows
    source venv/bin/activate     # macOS / Linux
    ```
3. **Install dependencies**: Install dependencies from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations**: Create the necessary database tables.
    ```bash
    cd gym_django
    python manage.py migrate
    ```
5. **Run the server**: Start the development server.
    ```bash
    python manage.py runserver
    ```
6. **Access the app**: Open a web browser and navigate to `http://localhost:8000/` to reach the login page.

## App Usage

- **Register and log in**: Create a staff account from the registration page, then log in.
- **Add members**: Fill in the membership form with personal, fee and trainer details.
- **Manage members**: Open a member to view their details, update them or delete them.
- **Search**: Look up members by name.
- **Track attendance**: Record attendance each day and open a member's monthly attendance report.

## Contributing

* Contributions are welcome! Feel free to fork the repository and submit a pull request for any improvements.
