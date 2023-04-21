# Pluto Learning User and Authentication Service

This is the user management and authentication service for the Pluto Learning platform.

---

## Getting Started

### Prerequisites

- [python3.11+](https://www.python.org/downloads/)
- [docker and docker-compose](https://docs.docker.com/get-docker/)
- Running on a linux machine or WSL(1 or 2) is recommended

---

## Running the Service

### Running Locally

1. Clone the repository

    ```bash
    git clone [repository url]
    ```

2. Create a virtual environment

    ```bash
    python3 -m venv .venv
    ```

3. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```

4. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Run the service

    ```bash
    make devG 
    # This will run the service with 20 workers and 1 master process

    make dev 
    # This will run the service with 1 worker and 1 master process

    make docker
    # This will build and run the service in a docker container
    ```

6. Clean up after running the service

    ```bash
    make clean
    ```

---

## API Documentation

- Default Url: <http://localhost:2000>

- Base Endpoints

```bash
[GET] /api/v1
[GET] /api/v1/health
```
