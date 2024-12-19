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
   git clone https://github.com/yourusername/employee-management-system.git

sample output
### Login
![Login Image](sample_output/login.png)

### Dashboard
![Dashboard Image](sample_output/dashboard.png)

### Add Employee
![Add Employee Image](sample_output/add.png)

### Edit Employee
![Edit Employee Image](sample_output/edit.png)

### Employee List
![Employee List Image](sample_output/employeelist.png)
