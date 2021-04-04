from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('aboutus.html')
@app.route("/contact")
def contact():
    return render_template('contactus.html')
@app.route("/semester1")
def semester1():
    return render_template('semester1.html')
@app.route("/semester2")
def semester2():
    return render_template('semester2.html')
@app.route("/semester3")
def semester3():
    return render_template('semester3.html')
@app.route("/c")
def c():
    return render_template('1c.html')
@app.route("/dp")
def dp():
    return render_template('1dp.html')
@app.route("/wbtechnologies")
def wb():
    return render_template('1webtechnologies.html')
@app.route("/effectivecommunication")
def effectivecommunication():
    return render_template('1effectivecommunication.html')
@app.route("/maths")
def maths():
    return render_template('1maths.html')


@app.route("/computerarchitecture")
def ca():
    return render_template('2computerarchitecture.html')
@app.route("/cpp")
def cpp():
    return render_template('2cpp.html')
@app.route("/datacommunication")
def dc():
    return render_template('2datacommunications.html')
@app.route("/datastructures")
def ds():
    return render_template('2datastructures.html')
@app.route("/probability")
def probability():
    return render_template('2probability.html')


app.run(debug=True)