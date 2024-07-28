# rule_engine/db.py
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb+srv://dandamudilokesh1234:fjnaYAzHOtKpzTjW@cluster0.xhmq9op.mongodb.net/')
    db = client['rule_engine_db']
    return db

def create_sample_data(db):
    rules_collection = db['rules']
    sample_rules = [
        {
            "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
            "description": "Sample rule 1",
            "created_at": "2024-07-23"
        },
        {
            "rule_string": "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)",
            "description": "Sample rule 2",
            "created_at": "2024-07-23"
        }
    ]
    rules_collection.insert_many(sample_rules)

def insert_rule(db, rule_string, description):
    rules_collection = db['rules']
    rule = {
        "rule_string": rule_string,
        "description": description,
        "created_at": "2024-07-23"
    }
    rules_collection.insert_one(rule)

def get_rules(db):
    rules_collection = db['rules']
    return list(rules_collection.find())

def get_rules_names(db, rule_names=None):
    rules_collection = db['rules']
    if rule_names:
        rules = rules_collection.find({'description': {'$in': rule_names}})
    else:
        rules = rules_collection.find()
    return list(rules)

def get_rule_by_id(db, rule_id):
    rules_collection = db['rules']
    from bson.objectid import ObjectId
    return rules_collection.find_one({"_id": ObjectId(rule_id)})

if __name__ == "__main__":
    db = get_db()
    create_sample_data(db)
