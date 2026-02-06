from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_zero.schemas import *
from http import HTTPStatus

app = FastAPI()

@app.get('/',status_code=HTTPStatus.OK,response_model=Message)
def read_root():
    return {'message':'Olá mundo!'}

@app.get('/html',status_code=HTTPStatus.OK,response_class=HTMLResponse)
def return_html():
    return """
<html>
    <head>
        <title> Olá mundo, agora em html </title>
    </head>
    <body>
        <h1>Olá mundo</h1>
    </body>
</html>"""

database = []

@app.post('/users/',status_code=HTTPStatus.CREATED,response_model=UserPublic)
def create_user(user:UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )
    database.append(user_with_id)
    return user_with_id
