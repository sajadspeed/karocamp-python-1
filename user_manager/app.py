from flask import Flask, render_template
import user_manager

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def home_page():
    title = "User Manager"
    return render_template("home.html", title=title)


@app.route("/users")
def users_page():
    users = user_manager.get_users()
    return render_template("users.html", users=users)


@app.route("/register-user")
def register_user_page():
    return render_template("register-user.html")


if __name__ == "__main__":
    app.run(port=80, debug=True)
