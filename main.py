from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # import the CORSMiddleware
from pydantic import BaseModel

import requests
import json

class EmailSchema(BaseModel):
    email: str

app = FastAPI()

# Add CORS Middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

API = "39481f9e97d7414ea3d674030f2e5483"

def get_email_data(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API}&email={email}"
    response = requests.get(url)
    emailData = json.loads(response.text)
    return emailData

def quality_score(emailData):
    q = emailData["quality_score"]
    e = emailData["email"]
    d = emailData["deliverability"].lower()
    return {"email": e, "deliverability": d, "quality_score": q}

@app.post("/verify_email")  
def verify(email_data: EmailSchema):  
    try:
        email = email_data.email  

        emailData = get_email_data(email)
        result = quality_score(emailData)
        return result
    except ValueError as ve:
        print(ve)
        return {"error": "Invalid email format"}
    except requests.exceptions.RequestException as e:
        print(e)
        return {"error": "Error contacting email validation API"}  
