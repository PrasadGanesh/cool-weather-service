import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def index():
    return "hello world"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
