# from rule_engine.parser import create_rule
# from rule_engine.evaluator import evaluate_rule
# from rule_engine.combiner import combine_rules

# def main():
#     rule1 = "age > 30 AND department = 'Sales'"
#     rule2 = "salary > 20000"
#     data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

#     # Create individual rules
#     ast1 = create_rule(rule1)
#     ast2 = create_rule(rule2)

#     # Combine rules
#     combined_ast = combine_rules([rule1, rule2])

#     # Evaluate rule
#     result = evaluate_rule(data, combined_ast)
#     print("Evaluation Result:", result)  # Expected output: True or False

# if __name__ == "__main__":
#     main()


# rule_engine/main.py


# rule_engine/main.py
from rule_engine.parser import create_rule
from rule_engine.evaluator import evaluate_rule
from rule_engine.combiner import combine_rules
from rule_engine.db import get_db, insert_rule, get_rules, get_rules_names

def main():
    db = get_db()

    # Insert rules into the database
    # rule1 = "age > 30 AND department = 'Sales'"
    # rule2 = "salary > 20000"
    # insert_rule(db, rule1, "Sample rule 1")
    # insert_rule(db, rule2, "Sample rule 2")

    # Retrieve rules from the database
    names = ["Sample rule 1", "AgeRule"]
    rules = get_rules_names(db, names)
    rule_strings = [rule['rule_string'] for rule in rules]


    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

    # Create and combine rules
    asts = [create_rule(rule_string) for rule_string in rule_strings]
    combined_ast = combine_rules(rule_strings)


    # Evaluate rule
    result = evaluate_rule(data, combined_ast)
    print("Evaluation Result:", result)  # Expected output: False

if __name__ == "__main__":
    main()

