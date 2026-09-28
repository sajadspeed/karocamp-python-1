from flask import Flask, render_template, request
import user_manager

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def home_page():
    title = "User Manager"
    return render_template("home.html", title=title)


@app.route("/users", methods=["POST", "GET"])
def users_page():
    users = []
    username_for_search = request.form.get("username")

    print(username_for_search)

    if username_for_search is None:
        users = user_manager.get_users()
    else:
        user = user_manager.find_user(username_for_search)
        if user is not None:
            users.append(user)

    return render_template("users.html", users=users)


@app.route("/register-user")
def register_user_page():
    return render_template("register-user.html")


if __name__ == "__main__":
    app.run(port=80, debug=True)
