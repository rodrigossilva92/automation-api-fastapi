# Automation API with FastAPI

This project demonstrates a backend automation API built with FastAPI.
It allows clients to submit automation tasks, process them asynchronously,
and retrieve execution status and results.

## Features
- Asynchronous task execution
- Input validation
- Status tracking
- RESTful API design

## Example Use Case
Submit a data processing task and retrieve aggregated results once completed.

## Tech Stack
FastAPI, Python, Pydantic

## How to Run

This project uses Poetry for dependency management.

```bash
poetry install
poetry run uvicorn app.main:app --reload


