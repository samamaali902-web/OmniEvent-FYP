from fastapi import FastAPI
from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated
from planner import create_event_plan

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

    plan = create_event_plan(
        event.event_type,
        event.budget,
        event.guest_count,
        event.location
    )

    return {
        "message": "Event plan generated successfully",
        "plan": plan
    }