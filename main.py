# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_home():
    return {"message": "Welcome to the Home Page"}

@app.get("/contact")
def read_contact():
    return {"message": "Contact us at: contact@example.com"}

@app.get("/about")
def read_about():
    return {"message": "This is a sample FastAPI app."}
