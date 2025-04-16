from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi = round(calculate_bmi(weight, height), 2)
            category = get_bmi_category(bmi)
        except ValueError:
            bmi = "Invalid input"
            category = "Please enter valid numbers."
    return render_template('index.html', bmi=bmi, category=category)

@app.route('/introduction')
def introduction():
    return render_template('intro.html')


@app.route('/pros-cons')
def pros_cons():
    return render_template('pros_cons.html')

if __name__ == '__main__':
    app.run(debug=True)