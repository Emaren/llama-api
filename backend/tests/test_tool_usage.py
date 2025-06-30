from backend.tools.tool_usage_logger import log_tool_usage, tool_log

def test_log_tool_usage():
    tool_log.clear()
    log_tool_usage("summarizer", "agent_123", {"text": "Hello"})
    assert len(tool_log) == 1
    assert tool_log[0]["tool"] == "summarizer"
    assert tool_log[0]["agent"] == "agent_123"
