from fastapi import FastAPI 
from pydantic import EmailStr

import requests
import json

app = FastAPI()

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

@app.get("/verify_email/{email}")  # {email} will be the user input on the Webflow site
def verify(email: str):
    try:
        # Basic validation using Pydantic's EmailStr type
        email = EmailStr(email)  # This will raise EmailNotValidError if the format is incorrect

        emailData = get_email_data(email)
        result = quality_score(emailData)
        return result
    except ValueError:
        return {"error": "Invalid email format"}
    except requests.exceptions.RequestException as e:
        return {"error": "Error contacting email validation API"}  # Handle potential network errors
