# 🖥️ Django Admin Dashboard (Multi-language)

## 📌 About the Project
This project is a **Django-based admin dashboard** that supports **multi-language (English & Persian)**.  
It is designed with a **clean class-based structure** and provides an easy-to-use panel for managing content and system features.  

---

## ⚡ Features & File Structure

### Main Features
- 🌍 **Multi-language support** (English & Persian).  
- 🛠️ **Class-based views** for better maintainability.  
- 📊 **Admin dashboard** with a modern design.  
- 📂 **Modular structure** for easy extension.  

### File Structure
```bash
project-root/
│── manage.py
│── requirements.txt
│── README.md
│── my_site/                # Main app (views, models, templates, static files)
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
│── blog/                   # Blog application
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
│── config/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── locale/                 # Translation files (English, Persian)
```

---

## 🚀 Getting Started

Follow the steps below to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py migrate
```

### 5️⃣ Run the development server
```bash
python manage.py runserver
```

Now open **http://127.0.0.1:8000/** in your browser 🚀  

---

## 📜 License
This project is licensed under the MIT License.
