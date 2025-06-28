from flask import Flask, url_for, render_template, redirect
from forms import Contact
from datas import data, add_data

app = Flask(__name__)
app.config["SECRET_KEY"] = "1728fea11de1f2131857e082921c20ae"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        add_data(form.fullname.data, form.email.data, form.mobile.data, form.message.data)
        return render_template("home.html")
    return render_template("contact.html", form=form)

@app.route("/admin")
def admin():
    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)