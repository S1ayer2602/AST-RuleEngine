import re
from rule_engine.my_ast import Node

def evaluate_node(node, data):
    if node.type == "operand":
        condition = node.value
        attribute, operator, value = re.split(r'([><=])', condition)
        attribute = attribute.strip()
        value = value.strip().strip("'")
        if operator == '>':
            return data[attribute] > int(value)
        elif operator == '<':
            return data[attribute] < int(value)
        elif operator == '=':
            return data[attribute] == value
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_node(node.left, data) and evaluate_node(node.right, data)
        elif node.value == "OR":
            return evaluate_node(node.left, data) or evaluate_node(node.right, data)
    return False

def evaluate_rule(json_data, rule_ast):
    return evaluate_node(rule_ast, json_data)
