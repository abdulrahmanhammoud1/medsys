# 🏥 MedSys API

🔗 **Live Demo:** [https://medsys-qvpu.onrender.com](https://medsys-qvpu.onrender.com)  
📘 **Swagger Docs:** [https://medsys-qvpu.onrender.com/api/docs/swagger/](https://medsys-qvpu.onrender.com/api/docs/swagger/)  
📗 **ReDoc Docs:** [https://medsys-qvpu.onrender.com/api/docs/redoc/](https://medsys-qvpu.onrender.com/api/docs/redoc/)

**MedSys** is a FHIR-inspired REST API for managing **patients**, **practitioners**, and **appointments** in a healthcare system.  
Built with **Django REST Framework**, it includes **JWT authentication**, **Celery + Redis background tasks**, and **Swagger/Redoc documentation**.

---

## 🚀 Features

- CRUD operations for Patients, Practitioners, and Appointments  
- JWT-based authentication for secure API access  
- Background email reminders using Celery & Redis  
- Auto-generated API documentation (Swagger & Redoc)  
- PostgreSQL or SQLite database support  
- Clean modular Django REST architecture  

---

## 🧩 Tech Stack

- **Backend:** Django 5 + Django REST Framework  
- **Database:** PostgreSQL (SQLite optional for demo)  
- **Task Queue:** Celery + Redis  
- **Authentication:** JWT (SimpleJWT)  
- **Docs:** drf-spectacular (Swagger / Redoc)  

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/abdulrahmanhammoud1/medsys.git
cd medsys