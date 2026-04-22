# 🤖 Python API Testing Framework (Pytest + HTML Report)

A lightweight and scalable **API automation testing framework** built using Python, Pytest, and Requests.  
It validates REST APIs and generates a detailed **HTML test execution report** using `pytest-html`.

---

## 🚀 Features

- ✅ API testing using Pytest  
- 🌐 REST API validation using Requests  
- 📊 HTML report generation (pytest-html)  
- 🧩 Simple and modular test structure  
- ⚡ Fast execution with clean assertions  
- 📦 Easy to extend for CI/CD integration  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Test Framework:** Pytest  
- **HTTP Client:** Requests  
- **Reporting:** pytest-html  

---

## 📂 Project Structure

```
python_api_testing/
│── config/
│   └── dev.json
│   └── stage.json
│   └── test.json
│── data/
│   ├── posts.json
│   ├── users.json
│── logs/
│   ├── api_test.log
│── tests/
│   ├── test_posts.py
│   ├── test_users.py
│── utils/
│   ├── api_client.py
│   ├── data_loader.py
│   └── json_validator.py
│── conftest.py
│── pytest.ini
│── README.md
│── requirements.txt
```

---

## ⚙️ Setup Instructions

### Clone Repository
```Terminal
git clone https://github.com/DilendraBarman/python_api_testing.git  
cd python_api_testing  
```

---

### Create Virtual Environment

```Terminal
python -m venv venv  
```
Mac/Linux:
```Terminal
source venv/bin/activate  
```
Windows:
```Terminal
venv\Scripts\activate  
```

---

### Install Dependencies

```Terminal
pip install -r requirements.txt  
```
---

## ▶️ Running Tests

Run all tests:
```Terminal
pytest  
```

Run with HTML report:
```Terminal
pytest --html=report.html --self-contained-html  
```

---

## 📊 Test Report

After execution, report is generated as:

report.html  

Summary:
- Total Tests: 3  
- Passed: 3  
- Failed: 0  
- Duration: ~641 ms  

---

## 📌 Sample Test Cases

### GET Users API
```Terminal
def test_get_users():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200  
```

---

### CREATE User API
```Terminal
def test_create_user():
    payload = {"name": "John"}
    response = requests.post("https://api.example.com/users", json=payload)
    assert response.status_code == 201  
```

---

## 📈 Future Improvements

- GitHub Actions CI pipeline  
- Allure reporting integration  
- JWT/OAuth authentication tests  
- JSON schema validation  
- Data-driven testing  

---

## 🛡️ Best Practices

- Do NOT commit report.html  
- Use environment variables for APIs  
- Keep tests modular  
- Follow AAA pattern  

---

## 🛡️ Disclaimer

This project is for learning and portfolio purposes only.

---

## ⭐ Support

If you find this useful, give it a ⭐ on GitHub.