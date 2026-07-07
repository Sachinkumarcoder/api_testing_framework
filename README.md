# API Testing Framework

Automated API testing framework using python, pytest, and requests library.

## Tech Stack
- Python 3.11
- pytest
- requests
- jsonschema
- python-dotenv
- pytest-html

## Project Structure
```
api_testing_framework/
│
├── .github/
│   └── workflows/
│       └── api_tests.yml
│
├── tests/
│   ├── test_posts.py
│   ├── test_users.py
│   ├── test_schema.py
│   └── test_negative.py
│
├── utils/
│   ├── api_client.py
│   └── schemas.py
│
├── reports/
├── conftest.py
├── pytest.ini
├── .env
├── .gitignore
└── README.md
```
## Setup

### 1. Setup Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate
```

### 2. Install packages 
```bash
pip install -r requirements.txt
```

### 3. Crete .env file
```
BASE_URL=https://jsonplaceholder.typicode.com
TIMEOUT=10
ENV=staging
```

## Tests Chalao

### Execue all tests
```bash
pytest
```

### Execute only smoke tests
```bash
pytest -m smoke
```

### Execute only regression tests
```bash
pytest -m regression
```

### Execute only negative tests
```bash
pytest -m negative
```

### Skip Slow tests
```bash
pytest -m "not slow"
```

### Specific file
```bash
pytest tests/test_posts.py
```

### HTML Report
```bash
pytest --html=reports/report.html
```

## Test Markers

| Marker     | Where to use                        |
|------------|-------------------------------------|
| smoke      | After deploy for quick sanity test  |
| regression | Full test suite                     |
| negative   | Error scenarios                     |
| slow       | Execute those tests which takes more|
|            | than 2 seconds                      |

## API Used
- Base URL: https://jsonplaceholder.typicode.com
- Free fake REST API for testing