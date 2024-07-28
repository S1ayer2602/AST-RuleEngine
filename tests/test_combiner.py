import unittest
from rule_engine.combiner import combine_rules
from rule_engine.parser import create_rule

class TestCombiner(unittest.TestCase):
    def test_combine_rules(self):
        rule1 = "age > 30 AND department = 'Sales'"
        rule2 = "salary > 50000"
        combined_ast = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_ast)

if __name__ == '__main__':
    unittest.main()
