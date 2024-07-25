from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Booking(BaseModel):
    user_id: str
    booking_time: datetime
    description: str
    recurring: Optional[bool] = False
    recurring_interval: Optional[str] = None  # e.g., "daily", "weekly"
    cancelled: Optional[bool] = False

