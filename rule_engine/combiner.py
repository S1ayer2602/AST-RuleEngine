from rule_engine.parser import create_rule
from rule_engine.my_ast import Node

def combine_two_rules(ast1, ast2, operator="AND"):
    return Node("operator", operator, ast1, ast2)

def combine_rules(rules):
    if not rules:
        return None
    if len(rules) == 1:
        return create_rule(rules[0])
    combined_ast = create_rule(rules[0])
    for rule in rules[1:]:
        new_ast = create_rule(rule)
        combined_ast = combine_two_rules(combined_ast, new_ast)

    return combined_ast
