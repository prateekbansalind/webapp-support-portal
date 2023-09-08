
---

# Customer Support Portal Web Service

This repository contains the Flask web application for our Customer Support Portal. It serves as an interface for our customers to seek support, get answers to frequently asked questions, raise tickets, and provide feedback.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running with Docker](#running-with-docker)
- [Accessing the Application](#accessing-the-application)

## Features

- **Home Page**: Introduction and guidelines for seeking support.
- **FAQ Page**: Frequently Asked Questions on orders, returns, payments, etc.
- **Ticketing Page**: Allows customers to raise support tickets.
- **Feedback Page**: Allows customers to leave feedback or reviews about products and services.

## Prerequisites

- Python 3.8 or newer
- Flask
- Docker (for containerized deployment)

## Setup & Installation

1. Clone this repository:
```bash
git clone https://github.com/prateekbansalind/webapp-support-portal.git
```

2. Navigate to the project directory:
```bash
cd webapp-support-portal
```

3. Run the Flask application:
```bash
python app.py
```

## Running with Docker

1. Build the Docker image:
```bash
docker build -t support-webapp:v1.0 .
```

2. Run the container:
```bash
docker run -p 8080:80 support-webapp:v1.0
```

## Accessing the Application

The application should be accessible at: [http://localhost:8080/]

