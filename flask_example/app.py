from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    my_title = "Asgar"
    bg_color = "#983274"
    return render_template("home.html", title=my_title, bg_color=bg_color)


@app.route("/hello")
def hello_page():
    return "<h1>Kooft</h1>"


@app.route("/users")
def users_page():
    users = [
        {"name": "Roya", "age": 26, "phone": "091356483124", "weight": 55},
        {"name": "Nastaran", "age": 32, "phone": "09382224781", "weight": 60},
        {"name": "Ali", "age": 40, "phone": "Not found", "weight": 98},
    ]
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(port=80, debug=True)
