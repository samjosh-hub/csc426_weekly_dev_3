from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "iro_secret_key"

DATABASE = "database.db"


# -----------------------------
# Database Initialization
# -----------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL,
            community TEXT NOT NULL,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date_reported TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Create the database when the application starts
init_db()


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
# Report Issue
# -----------------------------
@app.route("/report", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        community = request.form["community"]
        category = request.form["category"]
        title = request.form["title"]
        description = request.form["description"]

        date_reported = datetime.now().strftime("%d-%m-%Y %H:%M")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO issues
            (fullname, email, community, category, title, description, date_reported)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            fullname,
            email,
            community,
            category,
            title,
            description,
            date_reported
        ))

        conn.commit()
        conn.close()

        flash("Issue submitted successfully!", "success")

        return redirect(url_for("report"))

    return render_template("report.html")


# -----------------------------
# View Reports
# -----------------------------
@app.route("/reports")
def reports():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM issues
        ORDER BY id DESC
    """)

    issues = cursor.fetchall()

    conn.close()

    return render_template("reports.html", issues=issues)


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)