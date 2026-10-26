from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EventRequest(BaseModel):
    event_type: str
    budget: int
    guest_count: int
    location: str


@app.get("/")
def home():
    return {"message": "Welcome to OmniEvent API"}


@app.post("/events/plan")
def plan_event(event: EventRequest):
    return {
        "message": "Event details received successfully",
        "event": event
    }