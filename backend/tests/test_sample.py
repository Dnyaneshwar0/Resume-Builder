# tests/test_sample.py

import unittest
from cover_letter.generator import generate_cover_letter
from formatter.latex_formatter import format_to_latex
from optimizer.content_optimizer import optimize_content
from parser.resume_parser import parse_resume
from scorer.ats_scorer import score_resume_against_job
from utils.helpers import read_file, save_file

class TestResumeBuilder(unittest.TestCase):

    def test_cover_letter(self):
        result = generate_cover_letter("Alice", "Engineer", "OpenAI", ["Python", "ML"])
        self.assertIn("OpenAI", result)

    def test_format_latex(self):
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "123-456",
            "experience": "Did X at Y",
            "education": "BS CS",
            "skills": ["Python", "ML"]
        }
        latex = format_to_latex(data)
        self.assertIn(r"\section*", latex)

    def test_optimizer(self):
        optimized = optimize_content("worked on projects")
        self.assertIn("collaborated", optimized)

    def test_parser(self):
        sample = "Alice\nalice@example.com\n123-456\nExperience line\nEdu line\nPython, ML"
        result = parse_resume(sample)
        self.assertEqual(result["name"], "Alice")
        self.assertIn("Python", result["skills"][0])

    def test_scorer(self):
        score, matched = score_resume_against_job(["Python", "ML"], ["Python", "AI"])
        self.assertGreaterEqual(score, 50)

if __name__ == "__main__":
    unittest.main()
