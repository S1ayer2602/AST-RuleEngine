import unittest
from rule_engine.my_ast import Node

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node("operand", "age > 30")
        self.assertEqual(node.type, "operand")
        self.assertEqual(node.value, "age > 30")

if __name__ == '__main__':
    unittest.main()
