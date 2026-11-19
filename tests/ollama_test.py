from ollama_chat import ask_capital
from tests.llm_as_judge import llm_as_a_judge_agrees
import unittest

class TestLLMResponse(unittest.TestCase):

    # WRONG MODEL    

    def test_unknown_model_returns_failure(self):
        response = ask_capital("Sweden", "no-such-model")
        self.assertEqual(response, "Failure.")

    # CONSISTENCY TEST: SWEDEN
    def test_knows_capital_of_sweden(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Sweden")
            if "Stockholm" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

    # CONSISTENCY TEST: AUSTRALIA
    def test_knows_capital_of_australia(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Australia")
            if "Canberra" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

    # LLM AS A JUDGE: SWEDEN 
    def test_judge_accepts_right_capital_sweden(self):
        answer = "The capital of Sweden is Stockholm."
        self.assertTrue(llm_as_a_judge_agrees("Sweden", answer, "Stockholm"))

    # LLM AS A JUDGE: AUSTRALIA
    def test_judge_accepts_right_capital_australia(self):
        answer = "The capital of Australia is Canberra."
        self.assertTrue(llm_as_a_judge_agrees("Australia", answer, "Canberra"))

    # HALLUCINATIONS 
    def test_judge_rejects_invented_capital(self):
        answer = "The capital of Bealandia is Bea City."
        self.assertFalse(llm_as_a_judge_agrees("Bealandia", answer, "There is no such country, so it has no capital."))


if __name__ == "__main__":
    unittest.main()