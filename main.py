from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class Booking(BaseModel):
    user_id: str
    booking_time: datetime
    description: str
    recurring: Optional[bool] = False

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/bookings/")
def create_booking(booking: Booking):
    return booking

