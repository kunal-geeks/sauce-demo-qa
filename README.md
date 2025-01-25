# Sauce Demo QA

This project is a **Test Automation Framework** built using **Selenium** and **Python** for automating tests on the Sauce Demo application. It is designed to ensure efficient test execution, detailed reporting, and maintainability.

---

## Objective

- Automate end-to-end testing of the Sauce Demo application.
- Validate critical functionalities such as login, logout, and navigation.
- Provide a reusable framework for scalable test automation.

---

## Tools & Technologies

- **Programming Language**: Python
- **Test Framework**: Pytest
- **Automation Library**: Selenium
- **Reporting**: Allure Reports
- **Utilities**:
  - Custom logging
  - Dynamic element handling with wait utilities
  - Parallel test execution using `pytest-xdist`

---

## Features

- **Page Object Model (POM)** for modular and maintainable test scripts.
- **Custom Wait Utilities** for reliable handling of dynamic elements.
- **Interactive Allure Reports** for detailed test insights.
- **Parallel Test Execution** to reduce execution time.

---

## How to Set Up

- prerequisite - Clone this repo open the project in VScode editor

### 1. Create a Virtual Environment

Run the following commands to create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 2. Install Dependencies

Install all required dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

- Firstly delete the previous allure_report folder 

### 1. Run Tests

```bash
pytest --alluredir=allure_report
```

### 2. Generate Allure Report

```bash
allure serve allure_report
```

### 3. Run Tests in Parallel

```bash
pytest -n <number_of_parallel_processes> --alluredir=allure_report
```

## Conclusion

This framework simplifies UI automation for the Sauce Demo application, providing modular design, robust error handling, and detailed reporting. It can be extended to include additional test scenarios and integrated into CI/CD pipelines for automated execution.
