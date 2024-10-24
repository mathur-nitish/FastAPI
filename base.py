from fastapi import FastAPI


app = FastAPI()

@app.get("/getMsg")
def sayHi():
    return {"message":"Hello User"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)