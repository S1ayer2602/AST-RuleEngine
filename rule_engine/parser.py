from rule_engine.my_ast import Node
from rule_engine.tokenizer import tokenize

def parse_expression(tokens):
    if not tokens:
        return None

    token = tokens.pop(0)

    if token == '(':
        left = parse_expression(tokens)
        operator = tokens.pop(0)
        right = parse_expression(tokens)
        tokens.pop(0)  # Remove the closing parenthesis
        return Node("operator", operator, left, right)
    elif token in ("AND", "OR"):
        return Node("operator", token)
    else:
        # Handling operands and simple conditions like age > 30
        if tokens and tokens[0] in ('>', '<', '=', '!='):
            operator = tokens.pop(0)
            value = tokens.pop(0)
            return Node("operand", f"{token} {operator} {value}")
        else:
            return Node("operand", token)

def create_rule(rule_string):
    tokens = tokenize(rule_string)
    ast = parse_expression(tokens)
    return ast


# import ast
# import re
# from typing import Union

# class Node:
#     def __init__(self, type: str, left=None, right=None, value=None):
#         self.type = type
#         self.left = left
#         self.right = right
#         self.value = value

# def create_rule(rule_string: str) -> Node:
#     # Convert logical operators to valid Python syntax
#     rule_string = rule_string.replace('AND', 'and').replace('OR', 'or').replace('=', '==')
#     parsed = ast.parse(rule_string, mode='eval')
#     return _build_ast(parsed.body)

# def _build_ast(node: ast.AST) -> Node:
#     if isinstance(node, ast.BoolOp):
#         op_type = 'AND' if isinstance(node.op, ast.And) else 'OR'
#         left = _build_ast(node.values[0])
#         right = _build_ast(node.values[1])
#         return Node(type='operator', left=left, right=right, value=op_type)
#     elif isinstance(node, ast.Compare):
#         left = _build_ast(node.left)
#         right = _build_ast(node.comparators[0])
#         op_type = _get_op_type(node.ops[0])
#         return Node(type='operand', left=left, right=right, value=op_type)
#     elif isinstance(node, ast.Name):
#         return Node(type='variable', value=node.id)
#     elif isinstance(node, ast.Constant):
#         return Node(type='constant', value=node.value)
#     else:
#         raise ValueError(f"Unsupported AST node: {node}")

# def _get_op_type(op: ast.cmpop) -> str:
#     if isinstance(op, ast.Eq):
#         return '=='
#     elif isinstance(op, ast.NotEq):
#         return '!='
#     elif isinstance(op, ast.Lt):
#         return '<'
#     elif isinstance(op, ast.LtE):
#         return '<='
#     elif isinstance(op, ast.Gt):
#         return '>'
#     elif isinstance(op, ast.GtE):
#         return '>='
#     else:
#         raise ValueError(f"Unsupported comparison operator: {op}")


