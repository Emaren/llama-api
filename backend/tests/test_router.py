from backend.agents.task_router import route_task

def test_route_task():
    assert route_task("generation", {}) == "agent_generator"
    assert route_task("evaluation", {}) == "agent_critic"
    assert route_task("unknown", {}) == "agent_fallback"
