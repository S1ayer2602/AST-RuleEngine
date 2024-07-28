import unittest
from rule_engine.tokenizer import tokenize

class TestTokenizer(unittest.TestCase):
    def test_tokenize(self):
        rule_string = "age > 30 AND department = 'Sales'"
        tokens = tokenize(rule_string)
        expected_tokens = ['age', '>', '30', 'AND', 'department', '=', "'Sales'"]
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()
