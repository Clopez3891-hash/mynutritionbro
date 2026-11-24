"""MyNutritionBro - Sprint 1: log and view weight and food entries."""
from datetime import date, datetime

from flask import Flask, redirect, render_template, request, url_for

import database

app = Flask(__name__)
database.init_db()


def parse_date(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
    except ValueError:
        return None


@app.route("/")
def home():
    return redirect(url_for("weight"))


@app.route("/weight", methods=["GET", "POST"])
def weight():
    error = None
    form = {"log_date": date.today().isoformat(), "weight": ""}
    if request.method == "POST":
        form = {"log_date": request.form.get("log_date", "").strip(),
                "weight": request.form.get("weight", "").strip()}
        log_date = parse_date(form["log_date"])
        try:
            value = float(form["weight"])
        except ValueError:
            value = None
        if log_date is None:
            error = "Please enter a valid date."
        elif value is None or not 0 < value <= 1000:
            error = "Weight must be a number greater than 0 and at most 1000."
        else:
            database.add_weight(log_date, value)
            return redirect(url_for("weight", sort=request.args.get("sort", "newest")))
    sort = request.args.get("sort", "newest")
    entries = database.get_weights(newest_first=(sort != "oldest"))
    return render_template("weight.html", entries=entries, error=error, form=form, sort=sort)


@app.route("/food", methods=["GET", "POST"])
def food():
    error = None
    form = {"log_date": date.today().isoformat(), "food_name": "", "calories": ""}
    if request.method == "POST":
        form = {"log_date": request.form.get("log_date", "").strip(),
                "food_name": request.form.get("food_name", "").strip(),
                "calories": request.form.get("calories", "").strip()}
        log_date = parse_date(form["log_date"])
        try:
            calories = int(form["calories"])
        except ValueError:
            calories = None
        if log_date is None:
            error = "Please enter a valid date."
        elif not form["food_name"]:
            error = "Food name cannot be empty."
        elif calories is None or not 0 < calories <= 10000:
            error = "Calories must be a whole number between 1 and 10,000."
        else:
            database.add_food(log_date, form["food_name"], calories)
            return redirect(url_for("food"))
    return render_template("food.html", entries=database.get_foods(), error=error, form=form)


if __name__ == "__main__":
    app.run(debug=True)
