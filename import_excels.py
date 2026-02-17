import os
import pandas as pd
import sqlite3
import re

DB_NAME = "questions.db"
EXCEL_FOLDER = "excels"


def clean_table_name(name):
    #sanitizare nume 
    name = name.lower()
    name = re.sub(r'[^a-z0-9_]', '_', name)
    return name


def import_excels():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for file in os.listdir(EXCEL_FOLDER):
        if file.endswith(".xlsx"):
            path = os.path.join(EXCEL_FOLDER, file)
            table_name = clean_table_name(os.path.splitext(file)[0])

            # read Excel
            df = pd.read_excel(path,skiprows=7, header=None)
            
            print("FILE:", file)
            print(df.head())
            
            df = df.iloc[:, :4]
            df.columns = ["question", "answer1", "answer2", "answer3"]
            
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT,
                    answer1 TEXT,
                    answer2 TEXT,
                    answer3 TEXT
                )
            """)

            
            cursor.execute(f"DELETE FROM {table_name}")

            # insert rows
            for _, row in df.iterrows():
                cursor.execute(f"""
                    INSERT INTO {table_name}
                    (question, answer1, answer2, answer3)
                    VALUES (?, ?, ?, ?)
                """, (
                    row["question"],
                    row["answer1"],
                    row["answer2"],
                    row["answer3"]
                ))

            print(f"Imported: {table_name}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    import_excels()
    print("All Excel files imported.")
