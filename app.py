from flask import Flask, url_for, render_template, redirect, request
from forms import Contact, SignupForm, LoginForm
# from datas import data, add_data
# from users import users, add_users
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, engine

app = Flask(__name__)
app.config["SECRET_KEY"] = "1728fea11de1f2131857e082921c20ae"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:tana9861751892%40@localhost:3306/waterSupply"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    dob = db.Column(db.Date)
    password = db.Column(db.String(20))

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50)) 
    email = db.Column(db.String(100))
    number = db.Column(db.String)
    message = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = Users.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                return render_template("payment.html")

    return render_template("login.html", title="Login", form = form)

@app.route("/plans")
def plans():
    return render_template("plans.html")

@app.route('/subscribe_plan', methods=["POST"])
def subscribe_plan():
    plan = request.form.get("plan")
    plans = {
        "basic": {"id": "basic", "name": "Basic", "price": 99, "duration": "month"},
        "premium": {"id": "premium", "name": "Premium", "price": 199, "duration": "month"},
        "annual": {"id": "annual", "name": "Annual", "price": 1499, "duration": "year"},
    }
    return render_template("payment_page.html", plan_details=plans[plan])

@app.route('/process_payment', methods=["POST"])
def process_payment():
    plan_id = request.form.get("plan")
    payment_method = request.form.get("payment_method")

    plans = {
        "basic": "Basic",
        "premium": "Premium",
        "annual": "Annual"
    }
    plan_name = plans.get(plan_id, "Unknown")

    return render_template("payment_successful.html", plan_name=plan_name)


@app.route("/signup", methods=["GET","POST"])
def signup():
    form = SignupForm()
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        gender = request.form["gender"]
        dob = request.form["dob"]
        password = request.form["password"]
        
        new_user = Users(name=username, email=email, gender=gender, dob=dob, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html", title="SignUp", form = form)

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = Contact()
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        message = request.form["message"]

        new_message = Data(fullname=fullname, email=email, number=mobile, message=message)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("contact.html", form=form)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def admin():
    data = Data.query.all()
    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)