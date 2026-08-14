from neo4j import GraphDatabase
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(__file__).parent / ".env", override=True)

URI = os.getenv("URI")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

def test_connection():
    driver.verify_connectivity()
    print("✅ Successfully Connected to CognoDB!")

    with driver.session() as session:
        result = session.run("RETURN 'Connected to CognoDB!' AS message")
        print(result.single()["message"])

if __name__ == "__main__":
    test_connection()
    