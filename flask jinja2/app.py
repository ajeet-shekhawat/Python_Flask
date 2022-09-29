from flask import Flask, redirect,render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        English = float(request.form['English'])
        Math = float(request.form['Math'])
        Hindi = float(request.form['Hindi'])
        Science = float(request.form['Science'])
        total_score = (English + Math + Hindi + Science)/4
    return render_template("result.html",FinalScore=total_score)
    # return redirect(url_for('result', score = total_score))

# @app.route('/result/<int:score>')
# def result(score):
#     res = ""
#     if score < 40:
#         res = "Result: Pass, Score: " + str(score)
#     else:
#         res = "Result: Fail, Score: " + str(score)
#     return render_template("result.html",FinalScore=res) 

if __name__=='__main__':
    app.run(debug=True)