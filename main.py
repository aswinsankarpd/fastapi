from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
	return {'data':{'name':'aswin'}}


@app.get('/blog/unpublished')
def unpublished():
	return {'data':'These are unpublished blogs'}


@app.get("/blog/{id}/comments")
def comments(id:int):
	return 'Comments on blog with id: {}'.format(id)


@app.get('/blog/{id}')
def blog(id:int):
	return {'data':id} 



