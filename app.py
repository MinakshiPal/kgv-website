from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "kgv_secret_key_change_this_in_production"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/jewelry")
def jewelry():
    return render_template("jewelry.html")

@app.route("/custom-jewelry")
def custom_jewelry():
    return render_template("custom-jewelry.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        mobile = request.form.get("mobile", "").strip()
        interest = request.form.get("interest", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not mobile:
            flash("Name and Mobile Number are required.", "error")
            return redirect(url_for("contact"))

        flash("Thank you! We will contact you soon.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)