from flask import Flask, url_for, render_template, redirect
from forms import Contact, SignupForm, LoginForm
from datas import data, add_data
from users import users, add_users

app = Flask(__name__)
app.config["SECRET_KEY"] = "1728fea11de1f2131857e082921c20ae"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email in users.keys():
            if password == users[email]["password"]:
                return redirect(url_for("subscription")) 
    return render_template("login.html", title="Login", form = form)

@app.route("/plans")
def plans():
    return render_template("plans.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        add_users(form.email.data,form.username.data,form.password.data)
        return redirect(url_for("login"))
    return render_template("signup.html", title="SignUp", form = form)

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        add_data(form.fullname.data, form.email.data, form.mobile.data, form.message.data)
        return render_template("home.html")
    return render_template("contact.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)