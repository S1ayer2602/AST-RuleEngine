# AST-RuleEngine

This project is a simple 3-tier rule engine application consisting of a Simple UI, API, and Backend to determine user eligibility based on attributes like age, department, income, spend, etc. The system uses Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features

- **Rule Creation**: Create rules based on user attributes.
- **Rule Combination**: Combine multiple rules efficiently.
- **Rule Evaluation**: Evaluate rules against user attributes to determine eligibility.
- **Dynamic Rule Management**: Modify existing rules dynamically.
- **Database Integration**: Store rules and metadata in MongoDB.
- **REST API**: API endpoints for creating rules, fetching rules, and evaluating rules.
- **Responsive UI**: Simple and responsive UI to interact with the rule engine.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/rule-engine.git
cd rule-engine```bash
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
   
```bash
pip install -r requirements.txt
```

4. Start the Flask application:

```bash
python api.py
```

## API Endpoints

**Create Rule: POST /create_rule**

- **Request Body**: {"rule_name": "AgeRule", "rule_string": "(age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing')"}
- **Response**: {"message": "Rule created successfully"}

**Get Rules: GET /get_rules**
- **Response**: [{"_id": "...", "rule_name": "AgeRule", "rule_string": "..."}]

**Evaluate Rule: POST /evaluate**
- **Request Body**: {"ruleStrings": ["AgeRule"], "attributes": {"age": 32, "department": "Sales"}}
- **Response**: {"result": true}

