from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
	id: Optional[int] = 0
	name: str
	email: str
	phone: Optional[str] = None


app = FastAPI()


data = [
	User(id = 1, name = "Arthur", email = "arthurzera@zera.com"),
	User(id = 2, name = "Arthur 2", email = "arthurzera2@zera.com", phone = "(99)  9 9999-9999"),
	User(id = 3, name = "Arthur 3", email = "arthurzera3@zera.com"),
	User(id = 4, name = "Arthur 4", email = "arthurzera4@zera.com", phone = "(88) 8 8888-8888"),
	User(id = 5, name = "Arthur 5", email = "arthurzera5@zera.com"),
	User(id = 6, name = "Arthur 6", email = "arthurzera6@zera.com"),
]


@app.get('/')
async def root():
	return {"message":"This is an API built with FastAPI. Developer: arthurzera-s (Git and Linkedin)"}


@app.get('/users/me')
def read_me():
	return {"user":"Your user here."}


@app.get('/users/{user_id}')
def read(user_id: int):
	return {"user": [user for user in data if user.id == user_id]}


@app.get('/users/')
async def read_pagination(skip: int = 0, limit: int = 10):
	return {"users": data[skip: skip + limit]}


@app.post('/users')
def create_user(user:User):
	user.id = data[-1].id + 1
	data.append(user)
	return {"message":"User was created."}


@app.patch('/users/{user_id}')
def update(user_id:int, user: User):
	for i in range(len(data)):
		if data[i].id == user_id:
			data[i] = user
	return {"message": "User was updated."}


@app.delete('/users/{user_id}')
def delete(user_id: int):
	user = []
	for i in data:
		if i.id == user_id:
			user = i
	if user == []:
		return {"message": "User not found."}
	else:
		data.remove(user)
		return {"message": "User was deleted."}