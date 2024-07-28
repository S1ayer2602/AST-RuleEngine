from flask import Flask, request, jsonify, send_from_directory
from rule_engine.parser import create_rule
from rule_engine.evaluator import evaluate_rule
from rule_engine.combiner import combine_rules
from rule_engine.db import get_db, insert_rule, get_rules_names, get_rules
import os

app = Flask(__name__, static_folder='ui')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    rule_name = data.get('rule_name')
    if not rule_string or not rule_name:
        return jsonify({'error': 'Missing rule_string or rule_name'}), 400

    try:
        db = get_db()
        insert_rule(db, rule_string, rule_name)
        return jsonify({'message': 'Rule created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_rules', methods=['GET'])
def get_rules_endpoint():
    try:
        db = get_db()
        rules = get_rules(db)
        return jsonify(list(rules)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/evaluate', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    rule_names = data.get('rule_strings')
    attributes = data.get('attributes')
    if not rule_names or not attributes:
        return jsonify({'error': 'Missing rule_strings or attributes'}), 400

    try:
        db = get_db()
        rules = get_rules_names(db, rule_names)
        rule_strings = [rule['rule_string'] for rule in rules]
        print(len(rule_strings))
        print(rule_strings[0])
        asts = [create_rule(rule_string) for rule_string in rule_strings]
        combined_ast = combine_rules(rule_strings)
        result = evaluate_rule(attributes, combined_ast)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
