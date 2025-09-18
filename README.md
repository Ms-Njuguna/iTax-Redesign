# 📌 iTax Redesign

## Project Overview

**iTax Redesign** is a modern reimagining of Kenya’s iTax system with a clean, responsive UI and a robust backend.
This full-stack project improves:

- User Experience – simpler navigation, intuitive workflows
- Performance – optimized frontend with Vite + React
- Security – JWT authentication, password hashing
- Scalability – REST API powered by Flask & SQLAlchemy

---

## Tech Stack

**Frontend**
- Vite + React
- TailwindCSS
- React Router
- Formik + Yup for forms & validation

**Backend**
- Flask
- SQLAlchemy + Flask-Migrate
- Flask-Login + Flask-Bcrypt
- RESTful APIs with Flask-RESTful

**Database**
- PostgreSQL

---

## Installation & Setup

1. Clone the repo

```bash
git clone https://github.com/Ms-Njuguna/iTax-Redesign.git
cd iTax-Redesign
```

2. Backend Setup

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run migrations
flask db upgrade

# Start server
flask run
```

3. Frontend Setup

```bash
cd client
npm install
npm run dev
```

---

## Project Structure

```bash
iTax-Redesign/
│── client/         # React (Vite) frontend
│── server/         # Flask backend
│── migrations/     # Database migrations
│── LICENSE         # MIT License
│── README.md       # Project docs
```

---

## Features

- User authentication (login/register)
- Dashboard for tax filing
- Real-time form validation
- Responsive, mobile-first design
- Fast API communication (fetch + JSON)

---

## Contributing

Contributions are welcome! 🎉

1.Fork the repo
2.Create a new branch (feature/new-feature)
3.Commit changes
4.Push branch & open a PR

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Author

Ms-Njuguna
[🔗 GitHub](https://github.com/Ms-Njuguna) | [LinkedIn](https://www.linkedin.com/in/patricia-njuguna-76b697202?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2BPOMa0NDSZuAZenR71jb4w%3D%3D)



