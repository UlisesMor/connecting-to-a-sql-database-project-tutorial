import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

print(" Connected to database")

create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
"""

with engine.begin() as conn:
    conn.execute(text(create_table_sql))

print(" Table created")

insert_sql = """
INSERT INTO users (name, email)
VALUES
    ('Alice', 'alice@email.com'),
    ('Bob', 'bob@email.com'),
    ('Charlie', 'charlie@email.com');
"""

with engine.begin() as conn:
    conn.execute(text(insert_sql))

print("Data inserted")


df = pd.read_sql("SELECT * FROM users;", engine)

print("\nUsers table:")
print(df)

