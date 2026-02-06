from http import HTTPStatus
from fastapi.testclient import TestClient
from src.fast_zero.app import app

def test_read_root_return_ok_ola_mundo():
    client = TestClient(app) # Arrange

    response = client.get('/') # Act

    assert response.status_code == HTTPStatus.OK # Assert
    assert response.json() == {'message':'Olá mundo!'}

def test_read_root_return_html_ola_mundo():
    client = TestClient(app) # Arrange

    response = client.get('/html') # Act

    assert response.status_code == HTTPStatus.OK # Assert
    assert response.text == """
<html>
    <head>
        <title> Olá mundo, agora em html </title>
    </head>
    <body>
        <h1>Olá mundo</h1>
    </body>
</html>"""