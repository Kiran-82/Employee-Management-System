# Employee Management System

A web-based application built with Django for managing employee details efficiently. This system includes features for admin authentication, employee management, and user-friendly navigation. 

## Features
- **Admin Login:** Secure login for administrators.
- **Dashboard:** Centralized view for managing employees.
- **Employee Management:**
  - View a list of employees.
  - Add new employees.
  - Edit existing employee details.
- **Logout Functionality:** Securely log out from the admin panel.

## Technologies Used
- **Backend:** Django
- **Database:** Django's default SQLite database
- **Frontend:** HTML, CSS, Bootstrap

## Database Structure
- **Admin Login Table (`t_login`):** Stores admin credentials.
  - Fields: `sno`, `userName`, `Pwd`
- **Employee Details Table:** Manages employee information.
  - Fields: `Image`, `Name`, `Email`, `Mobile`, `Designation`, `Gender`, `Course`, `Createdate`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kiran-82/Employee-Management-System.git

sample output
### Login
![Login Image](sample%20output/login.png)

### Dashboard
![Dashboard Image](sample%20output/dashboard.png)

### Add Employee
![Add Employee Image](sample%20output/add.png)
### Add details
![Login fill](sample%20output/add%20details.png)
### Edit Employee
![Edit Employee Image](sample%20output/edit.png)

### Employee List
![Employee List Image](sample%20output/employee%20list.png)

### Employee List search
![Employee List Image](sample%20output/search.png)
