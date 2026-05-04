from flask import Flask, render_template_string, request
import smtplib

app = Flask(__name__)

html = """
<form method="POST">
    <input name="name" placeholder="Name" required><br><br>
    <input name="email" placeholder="Email" required><br><br>
    <input name="age" placeholder="Age" required><br><br>
    <button type="submit">Submit</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        message = f"Subject: New Form Data\\n\\nName: {name}\\nEmail: {email}\\nAge: {age}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login("ke2020682@gmail.com", "YOUR_APP_PASSWORD")

        server.sendmail(
            "kp2020682@gmail.com",
            "kp2020682@gmail.com",
            message
        )

        server.quit()

        return "Have a nice meet you!"

    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
