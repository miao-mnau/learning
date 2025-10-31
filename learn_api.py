from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, World! This is my first API!"}

@app.get("/ai-internship")
def get_internship_info():
    return{
        "company": "DTSE (T-Mobile)",
        "position":"AI Intern",
        "status": "We are learning FastAPI!"
    }
