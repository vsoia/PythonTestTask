# Python Practical Task 
The repository contains API and UI tests according to practical task after "Python QA Automation Course"

## Requirements

- Python 3.12+
- Pytest
- Requests
- Playwright

## Setup

1. Clone the repository (git clone <repo-url>)
2. Install modules 
    pip install -r requirements.txt
    playwright install
3. Add your own reqres API key to const with name "API_KEY" in conftest.py for API calls

## Running tests

1. Run API tests from cli:
    ```bash 
   pytest -v tests/api 
   ```
2. Run UI tests from cli:
   ```bash  
   pytest -v tests/ui
      ```
   
