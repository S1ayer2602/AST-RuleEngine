import unittest
from rule_engine.parser import create_rule

class TestParser(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

if __name__ == '__main__':
    unittest.main()
