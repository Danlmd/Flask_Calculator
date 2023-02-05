from flask import Flask, render_template, request
import functions

app = Flask(__name__)
app.secret_key = "asdklfsdlakfsdjklf2312"

@app.route("/")
@app.route("/classic")
def home():
    return render_template("main.html")

@app.route("/classic_result",methods=['POST'])
def classic():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = functions.calculating(a,b,operation)

    return render_template('main.html', prediction_text=str(result))


@app.route("/quadratic")
def home2():
    return render_template("quadratic.html")
    
@app.route("/quadratic_result",methods=['POST'])
def quadratic():

    a = request.form['a']
    b = request.form['b']
    c = request.form['c']

    result = functions.quadratic_formula(a,b,c)

    return render_template('quadratic.html', prediction_text=str(result))

@app.route("/pythagorean")
def home3():
    return render_template("pythagorean.html")

@app.route("/pythagorean_result",methods=['POST'])
def pythagorean():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']

    result = functions.pythagorean_theorem(a,b,c)

    return render_template('pythagorean.html', prediction_text=str(result))

@app.route("/bmi")
def home4():
    return render_template("bmi.html")
    
@app.route("/bmi_result",methods=['POST'])
def bmi():

    height = request.form['height']
    weight = request.form['weight']

    result = functions.bmi(height, weight)

    return render_template('bmi.html', prediction_text=str(result))



if __name__ == "__main__":
    app.run(debug=True)