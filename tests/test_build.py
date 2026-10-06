import unittest
from scripts.build import link, render

class BuildTests(unittest.TestCase):
    def test_rejects_script_urls(self):
        with self.assertRaises(ValueError):
            link("javascript:alert(1)", "unsafe")

    def test_escapes_profile_text(self):
        data = {"basics": {"name": "<script>alert(1)</script>", "label": "Engineer", "summary": '"<b>hello</b>', "email": "test@example.com"}}
        html = render(data)
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("&quot;&lt;b&gt;", html)

if __name__ == "__main__":
    unittest.main()
