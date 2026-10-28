from fastapi import FastAPI
from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated

app = FastAPI()

class EventRequest(BaseModel):
    event_type: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    budget: int = Field(gt=0)
    guest_count: int = Field(gt=0)
    location: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

@app.get("/")
def home():
    return {"message": "Welcome to OmniEvent API"}


@app.post("/events/plan")
def plan_event(event: EventRequest):
    return {
        "message": "Event details received successfully",
        "event": event
    }