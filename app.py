from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB = "questions.db"

def get_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]

    conn.close()
    return render_template("index.html", chapters=tables)


@app.route("/chapter/<table>")
def show_chapter(table):
    q = int(request.args.get("q", 1))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    total = cursor.fetchone()[0]

    cursor.execute(f"SELECT * FROM {table} LIMIT 1 OFFSET ?", (q - 1,))
    question = cursor.fetchone()

    print("QUESTION:", question)

    conn.close()

    return render_template(
        "chapter.html",
        table=table,
        question=question,
        q=q,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)
