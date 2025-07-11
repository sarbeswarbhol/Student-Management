
# 🎓 Student Management System

A modern and intuitive Django web application to manage student records, parent/guardian details, and class information — built with clean UI design and secure authentication system.

---

## 🎯 Live Demo

🔗 [Try Here](#)  
<!-- Replace # with your live link if deployed -->

---

## 🔍 Features

* 🔐 Secure login, registration, and password reset
* 👩‍🎓 Manage student and parent data (CRUD)
* 📸 Upload student images
* 🔎 Search and filter students easily
* 💻 Responsive and clean user interface
* 🛡️ Secure with Django’s built-in auth system

---

## 📸 Preview

### 🔹 Home Page
![Home Page](screenshots/127.0.0.1_8000_(Nest%20Hub%20Max).png)

### 🔹 Register  
![Register](screenshots/127.0.0.1_8000_authentication_signup_(Nest%20Hub%20Max).png)

### 🔹 Login  
![Login](screenshots/127.0.0.1_8000_authentication_login_(Nest%20Hub%20Max).png)

### 🔹 Forget Password  
![Forget Password](screenshots/127.0.0.1_8000_authentication_forgot-password_(Nest%20Hub%20Max).png)

### 🔹 Student  List 
![Student List](screenshots/127.0.0.1_8000_student_(Nest%20Hub%20Max).png)

### 🔹 Add Student  
![Add Student](screenshots/127.0.0.1_8000_student_add_(Nest%20Hub%20Max).png)


### 🔹 Student Details  
![Student Details](screenshots/127.0.0.1_8000_student_students_faa(Nest%20Hub%20Max).png)

---

## 🛠️ Technologies Used

**Frontend:**
- HTML5
- CSS3 (Bootstrap)
- JavaScript
- Google Fonts
- Icons (Font Awesome / Bootstrap Icons)

**Backend:**
- Django 3.2+
- SQLite3
- Python 3.8+

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/sarbeswarbhol/Student-Management

# Navigate to the project directory
cd Student-Management

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
````

---

## 📁 Project Structure

```
student-management/
├── home_auth/         # Handles login, registration, and password reset
├── student/           # Student CRUD operations and parent info
├── school/            # Additional school-related models/views
├── templates/         # HTML templates
│   ├── auth/
│   ├── student/
│   └── base.html
├── static/            # CSS, JS, images
├── screenshots/       # Screenshots used in README
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## 🤝 Contributing

Feel free to fork the project and submit pull requests. For major changes, open an issue to discuss the changes you’d like to make.

---

## 📄 License

This project is licensed under the **MIT License**.

---

> Developed with ❤️ using Django by Sarbeswar Bhol