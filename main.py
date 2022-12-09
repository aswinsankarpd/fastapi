from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
	return {'data':{'name':'aswin'}}


@app.get('/about')
def about():
	return "The about page"