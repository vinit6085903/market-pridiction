from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# other pages
@app.route("/signals")
def signals():
    return render_template("signals.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/markets")
def markets():
    return render_template("markets.html")

@app.route("/market-analysis")
def market_analysis():
    return render_template("market-analysis.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html")

if __name__ == "__main__":
    app.run(debug=True)
