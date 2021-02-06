# flask sample app

## APIs

1. GET /health
    ```json
    {"status":"healthy"}
    ```
1. GET /users?user_id=1
    ```json
    {
        "id": 1,
        "name": "test_user1"
    }
    ```

## Local Development

### With Local Python

1. Run MySQL

    ```
    docker-compose -f docker/docker-compose.yml up mysql -d
    ```

1. Local env

    ```
    python3 -m venv venv
    . venv/bin/activate
    cd src
    pip install -r sample/requirements.txt
    FLASK_APP=sample FLASK_ENV=development flask run
    ```

1. Curl

    ```
    curl localhost:5000/health
    {"status":"healthy"}
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
