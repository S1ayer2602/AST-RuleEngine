import unittest
from rule_engine.evaluator import evaluate_rule
from rule_engine.parser import create_rule

class TestEvaluator(unittest.TestCase):
    def test_evaluate_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(data, ast)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
