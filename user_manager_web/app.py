from flask import Flask, render_template, request, redirect, url_for, flash

import user_manager


app = Flask(__name__)


@app.route("/")
def index():
    username = request.args.get("username", "").strip()

    if username:
        users = []
        user = user_manager.find_user(username)

        if user is not None:
            users.append(user)
    else:
        users = user_manager.get_users()

    return render_template("index.html", users=users, username=username)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        name = request.form["name"].strip()
        age = int(request.form["age"])
        city = request.form["city"].strip()

        skills_input = request.form["skills"].strip()
        skills = []

        if skills_input:
            skills = [skill.strip() for skill in skills_input.split(",")]

        is_verified = "is_verified" in request.form

        result = user_manager.register_user(
            username,
            password,
            name,
            age,
            city,
            skills,
            is_verified
        )

        if result:
            flash("User registered successfully.", "success")
            return redirect(url_for("index"))

        flash("This username already exists.", "danger")

    return render_template("register.html")


@app.route("/users/<username>")
def user_detail(username):
    user = user_manager.find_user(username)

    if user is None:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    return render_template("user_detail.html", user=user)


@app.route("/users/<username>/update", methods=["GET", "POST"])
def update_profile(username):
    user = user_manager.find_user(username)

    if user is None:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form["name"].strip()
        age = int(request.form["age"])
        city = request.form["city"].strip()

        user_manager.update_profile(username, name, age, city)

        flash("Profile updated successfully.", "success")
        return redirect(url_for("user_detail", username=username))

    return render_template("edit_profile.html", user=user)


@app.route("/users/<username>/skills", methods=["POST"])
def add_skill(username):
    user = user_manager.find_user(username)

    if user is None:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    skill = request.form["skill"].strip()

    if skill:
        user_manager.add_skill(username, skill)
        flash("Skill added successfully.", "success")

    return redirect(url_for("user_detail", username=username))


@app.route("/users/<username>/verify", methods=["POST"])
def verify_user(username):
    result = user_manager.change_verification(username)

    if result:
        flash("User verification status changed.", "success")
    else:
        flash("User not found.", "danger")

    return redirect(url_for("user_detail", username=username))


@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    user = user_manager.find_user(username)

    if user is None:
        flash("User not found.", "danger")
        return redirect(url_for("index"))

    user_manager.delete_user(username)

    flash("User deleted successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
