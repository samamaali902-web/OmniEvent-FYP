def create_event_plan(event_type, budget, guest_count, location):

    venue_budget = budget * 0.40
    catering_budget = budget * 0.30
    decoration_budget = budget * 0.20
    photography_budget = budget * 0.10

    return {
        "event_type": event_type,
        "budget": budget,
        "guest_count": guest_count,
        "location": location,
        "budget_breakdown": {
            "venue": venue_budget,
            "catering": catering_budget,
            "decoration": decoration_budget,
            "photography": photography_budget
        },
        "planning_status": "Basic plan created"
    }