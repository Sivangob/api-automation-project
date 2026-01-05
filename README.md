# API Automation Project

This repository demonstrates a simple API automation testing project built with Python and pytest.
The focus of this project is on test structure, readability, and maintainability, using reusable API clients and a clear separation of concerns.

This is a demonstration project intended to showcase automation fundamentals rather than a production-grade testing solution.

## Tech Stack
- Python
- pytest
- requests

## What Is Covered
- API status code validation
- Response body assertions
- Handling of invalid requests
- Basic response time checks (for demonstration purposes only)

## Project Structure
- `src/` – reusable API clients and request logic
- `tests/` – pytest test cases and fixtures

## Installation
Install dependencies:
```bash
pip install -r requirements.txt

## Running the Tests

Run all tests using:

pytest

## Test Data Source

The tests use a public mock REST API for demonstration purposes:

https://jsonplaceholder.typicode.com

## Notes
- This project is intended for learning and demonstration purposes.
- It focuses on clean test organization and automation practices, not on full production coverage or performance testing.
