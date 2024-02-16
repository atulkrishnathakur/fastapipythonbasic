from fastapi.testclient import TestClient
import httpx
from main import app,get_db_session

testing_db = ["DB for testing"]


def get_testing_db():
    return testing_db 


app.dependency_overrides[get_db_session] = get_testing_db
client = TestClient(app)


def test_item_should_add_to_database():
    response = client.get(
        "/add-item/?item=sugar",
    )
    assert response.status_code == 200
    assert response.text == '{"message":"added item sugar"}'

# Run below command for unit test
# (venv) atul@atul-Lenovo-G570:~/myfastapi/di$ pytest -s
# assert is a python keyword that is used for unit testing. It is very good. 
# if error found then assert stop the execution of code

# https://fastapitutorial.com/blog/dependency-injection-fastapi/