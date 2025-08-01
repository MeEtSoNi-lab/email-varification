from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import re

app = FastAPI()

# Request schema
class EmailRequest(BaseModel):
    email: EmailStr

# Email validation logic
def is_disposable(email):
    disposable_domains = ['mailinator.com', 'tempmail.com', '10minutemail.com']
    domain = email.split('@')[1]
    return domain in disposable_domains

@app.post("/validate_email")
async def validate_email(data: EmailRequest):
    if is_disposable(data.email):
        return {"status": "Disposable", "email": data.email}
    return {"status": "Valid", "email": data.email}
