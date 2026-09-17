from flask import (
    Flask,
    render_template,
    abort,
    request,
    redirect,
    url_for,
    session,
    flash
)

import os
import sqlite3

from dotenv import load_dotenv
from werkzeug.security import check_password_hash


load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)


def get_db_connection():
    connection = sqlite3.connect("events.db")
    connection.row_factory = sqlite3.Row
    return connection


def get_event(event_id):
    connection = get_db_connection()

    event = connection.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    connection.close()

    if event is None:
        abort(404)

    return event


@app.route("/")
def home():
    connection = get_db_connection()

    events = connection.execute(
        "SELECT * FROM events ORDER BY date ASC"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        events=events
    )


@app.route("/event/<int:event_id>")
def event_detail(event_id):
    event = get_event(event_id)

    return render_template(
        "event_detail.html",
        event=event
    )


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()

        admin = connection.execute(
            "SELECT * FROM admins WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if admin and check_password_hash(
            admin["password_hash"],
            password
        ):
            session["admin_id"] = admin["id"]
            session["admin_username"] = admin["username"]

            return redirect(
                url_for("admin_dashboard")
            )

        flash("Username atau password salah.")

    return render_template("admin_login.html")


@app.route("/admin/dashboard")
def admin_dashboard():

    if "admin_id" not in session:
        return redirect(
            url_for("admin_login")
        )

    connection = get_db_connection()

    events = connection.execute(
        "SELECT * FROM events ORDER BY date ASC"
    ).fetchall()

    connection.close()

    return render_template(
        "admin_dashboard.html",
        events=events
    )

@app.route("/admin/event/create", methods=["GET", "POST"])
def create_event():

    if "admin_id" not in session:
        return redirect(url_for("admin_login"))

    if request.method == "POST":

        title = request.form["title"].strip()
        description = request.form["description"].strip()
        date = request.form["date"].strip()
        location = request.form["location"].strip()
        status = request.form["status"].strip()

        if not title:
            flash("Event title is required.")

        elif not description:
            flash("Description is required.")

        elif not date:
            flash("Event date is required.")

        elif not location:
            flash("Location is required.")

        elif status not in ["Upcoming", "Ongoing", "Completed"]:
            flash("Invalid event status.")

        else:

            connection = get_db_connection()

            connection.execute(
                """
                INSERT INTO events
                (title, description, date, location, status)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    title,
                    description,
                    date,
                    location,
                    status
                )
            )

            connection.commit()
            connection.close()

            flash("Event successfully created!")

            return redirect(
                url_for("admin_dashboard")
            )

    return render_template("create_event.html")

@app.route("/admin/event/<int:event_id>/edit", methods=["GET", "POST"])
def edit_event(event_id):

    if "admin_id" not in session:
        return redirect(url_for("admin_login"))

    event = get_event(event_id)

    if request.method == "POST":

        title = request.form["title"].strip()
        description = request.form["description"].strip()
        date = request.form["date"].strip()
        location = request.form["location"].strip()
        status = request.form["status"].strip()

        if not title:
            flash("Event title is required.")

        elif not description:
            flash("Description is required.")

        elif not date:
            flash("Event date is required.")

        elif not location:
            flash("Location is required.")

        elif status not in ["Upcoming", "Ongoing", "Completed"]:
            flash("Invalid event status.")

        else:

            connection = get_db_connection()

            connection.execute(
                """
                UPDATE events
                SET title = ?,
                    description = ?,
                    date = ?,
                    location = ?,
                    status = ?
                WHERE id = ?
                """,
                (
                    title,
                    description,
                    date,
                    location,
                    status,
                    event_id
                )
            )

            connection.commit()
            connection.close()

            flash("Event successfully updated!")

            return redirect(
                url_for("admin_dashboard")
            )

    return render_template(
        "edit_event.html",
        event=event
    )

@app.route("/admin/event/<int:event_id>/delete", methods=["POST"])
def delete_event(event_id):

    if "admin_id" not in session:
        return redirect(url_for("admin_login"))

    event = get_event(event_id)

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM events WHERE id = ?",
        (event_id,)
    )

    connection.commit()
    connection.close()

    flash(
        f'Event "{event["title"]}" successfully deleted!'
    )

    return redirect(
        url_for("admin_dashboard")
    )


@app.route("/admin/logout")
def admin_logout():

    session.clear()

    return redirect(
        url_for("admin_login")
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)