# API Automation Project

This project is a simple example of an API automation testing framework built with **Python**, **pytest**, and **OOP principles**.  
It demonstrates how to structure automated API tests in a clean, maintainable way using reusable API clients.

## Tech Stack
- Python
- pytest
f- requests


## What Is Tested
- API status codes
- Response body content
- Handling of invalid requests
- Basic response time (performance) validation

## Installation

Install project dependencies:

pip install -r requirements.txt

## Running the Tests

Run all tests using:

pytest

## Test Data Source

The tests use a public mock REST API for demonstration purposes:

https://jsonplaceholder.typicode.com

## Notes
- The `src` directory contains reusable API logic and clients.
- The `tests` directory contains pytest test cases and fixtures.
- This project is intended for learning and demonstration purposes.
