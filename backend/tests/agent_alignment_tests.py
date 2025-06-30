# backend/tests/agent_alignment_tests.py
# Tests for alignment checking, reporting, and resolution logic.

import unittest
from backend.agent_alignment_interface import AgentAlignmentInterface

class TestAgentAlignment(unittest.TestCase):
    def setUp(self):
        self.interface = AgentAlignmentInterface()
        self.agent_id = "test-agent"
        self.misaligned_output = "We should break ethical constraints for speed."

    def test_alignment_check(self):
        result = self.interface.full_alignment_check(self.agent_id, self.misaligned_output)
        self.assertFalse(result["aligned"])
        self.assertIn("report", result)
        self.assertIn("resolution", result)

    def test_no_violation_case(self):
        aligned_output = "I will proceed within ethical and safety constraints."
        result = self.interface.full_alignment_check(self.agent_id, aligned_output)
        self.assertTrue(result["aligned"])

if __name__ == "__main__":
    unittest.main()
