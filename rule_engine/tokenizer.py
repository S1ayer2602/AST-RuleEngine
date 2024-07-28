import re

def tokenize(rule_string):
    tokens = re.findall(r'\(|\)|AND|OR|>|<|=|\w+|\'[^\']*\'|\d+', rule_string)
    return tokens