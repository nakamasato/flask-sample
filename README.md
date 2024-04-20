# flask sample app

[![codecov](https://codecov.io/gh/nakamasato/flask-sample/branch/master/graph/badge.svg?token=07U6WH31WV)](https://codecov.io/gh/nakamasato/flask-sample)

![](diagram.drawio.svg)

## Versions
- Python: 3.12
- Flask: 3.0.3
## APIs

1. GET /health
    ```json
    {"status":"healthy"}
    ```
1. GET /users/1
    ```json
    {
        "id": 1,
        "name": "test_user1"
    }
    ```
1. POST /users/
    ```json
    curl -X POST -H "Content-Type: application/json" -d '{"name": "naka", "email": "naka@example.com"}' localhost:5000/users
    {
      "id": 7,
      "name": "naka"
    }
    ```

## Directory

- `sample/`, a Python package containing your application code and files.
- `tests/`, a directory containing test modules.
- `venv/`, a Python virtual environment where Flask and other dependencies are installed.
## Local Development

### With Local Python

1. Prepare requirements.txt

    ```
    poetry export -f requirements.txt --output requirements.txt --without-hashes
    ```

1. Run MySQL

    ```
    docker-compose -f docker/docker-compose.yml up -d mysql
    ```

1. Local env

    ```
    poetry install
    FLASK_APP=sample FLASK_ENV=development poetry run flask run
    ```

1. Check health

    ```
    curl localhost:5000/health
    {"status":"healthy"}
    ```

1. Run test

    ```
    poetry run pytest
    ========================================================================================== test session starts ==========================================================================================
    platform darwin -- Python 3.9.0, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/masato-naka/repos/nakamasato/flask-sample
    plugins: cov-3.0.0
    collected 3 items

    tests/test_api.py ...                                                                                                                                                                             [100%]

    =========================================================================================== 3 passed in 0.06s ===========================================================================================
    ```
### With Docker

1. Docker Compose

    ```
    docker-compose -f docker/docker-compose.yml up # add --build if you want to rebuild
    ```

1. Curl

    ```
    curl localhost:5000/health
    {"status":"healthy"}
    ```

## Test

- coverage: [codecov](https://app.codecov.io/) (https://app.codecov.io/gh/nakamasato/flask-sample)
