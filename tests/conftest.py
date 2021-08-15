import pytest
import os
import sys
import pymysql
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(
        str(pytestconfig.rootdir),
        "tests",
        "docker-compose.yml"
    )


def is_mysql_ready(host, port):
    try:
        connection = pymysql.connect(
            host=host,
            user='root',
            password='password',
            database='test',
            port=port,
        )
        with connection.cursor() as cursor:
            cursor.execute('show databases')
        return True
    except Exception as e:
        print(e)
        return False


@pytest.fixture(scope="session")
def mysql_service(docker_ip, docker_services):

    port = docker_services.port_for("mysql", 3306)
    docker_services.wait_until_responsive(
        timeout=60.0, pause=1, check=lambda: is_mysql_ready(docker_ip, port)
    )
    return docker_ip, port
