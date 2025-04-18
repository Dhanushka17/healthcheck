from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values")
    return weight / (height ** 2)
def calculate_bmr(gender,age,weight,height):
    if gender=='female':
        return 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)
    elif gender=='male':
        return 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)
    else:
        raise ValueError("Gender must be 'male' or 'female'")


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    error = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            
            # Validate input values
            if weight <= 0:
                raise ValueError("Weight must be a positive number")
            if height <= 0:
                raise ValueError("Height must be a positive number")
            if weight > 500:  # Unrealistic weight
                raise ValueError("Please enter a realistic weight (kg)")
            if height > 3:  # Unrealistic height in meters
                raise ValueError("Please enter a realistic height (m)")
                
            bmi = round(calculate_bmi(weight, height), 2)
            category = get_bmi_category(bmi)
        except ValueError as e:
            error_msg = str(e)
            if "could not convert" in error_msg.lower():
                error = "Please enter valid numbers."
            else:
                error = error_msg
            bmi = None
            category = None
    return render_template('index.html', bmi=bmi, category=category, error=error, title="BMI Calculator")

@app.route('/home')
def home():
    return render_template('HOME.html', title="Understanding BMI")

@app.route('/introduction')
def introduction():
    return render_template('intro.html', title="Introduction to BMI")

@app.route('/sustainable-engineering')
def sustainable_engineering():
    # Create this template if it doesn't exist
    return render_template('sustainable_engineering.html', title="Sustainable Engineering")

@app.route('/pros-cons')
def pros_cons():
    return render_template('pros_cons.html', title="Pros & Cons of BMI")

if __name__ == '__main__':
    app.run(debug=True)