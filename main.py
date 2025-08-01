from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
app = FastAPI()
class EmailRequest(BaseModel):
    email: EmailStr
@app.post("/validate_email")
async def validate_email(data: EmailRequest):
    return {"message": f"Email is: {data.email}"}
