import sqlite3

conn = sqlite3.connect("questions.db")
cursor = conn.cursor()

# cursor.execute("SELECT * FROM legislatie_gr__1_05_2023 LIMIT 5")
# rows = cursor.fetchall()
# print(rows)
# conn.close()

# debug route in app.py

# @app.route("/debug")
# def debug():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     # replace with your table name
#     table_name = "legislatie_gr__1_05_2023"

#     cursor.execute(f"SELECT * FROM '{table_name}' LIMIT 5")
#     rows = cursor.fetchall()
#     conn.close()

#     # return as plain text for easy checking
#     return "<pre>" + str(rows) + "</pre>"