from flask import Flask, render_template, request
 
app = Flask(__name__)
 
def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    if bmi < 18.5:

        category = "Underweight"

    elif 18.5 <= bmi < 24.9:

        category = "Normal"

    elif 25 <= bmi < 29.9:

        category = "Overweight"

    else:

        category = "Obese"

    return round(bmi, 2), category
 
@app.route("/", methods=["GET", "POST"])

def index():

    bmi = category = None

    if request.method == "POST":

        weight = float(request.form["weight"])

        height = float(request.form["height"])

        bmi, category = calculate_bmi(weight, height)

    return render_template("index.html", bmi=bmi, category=category)
 
if __name__ == "__main__":

    app.run(debug=True)

 