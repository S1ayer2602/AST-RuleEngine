# test_mongo.py
from pymongo import MongoClient

def test_mongo_connection():
    try:
        client = MongoClient('mongodb+srv://dandamudilokesh1234:fjnaYAzHOtKpzTjW@cluster0.xhmq9op.mongodb.net/')
        db = client['test_db']
        print("Successfully connected to MongoDB.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    test_mongo_connection()
