from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")



@app.route('/member')
def member():
    return "Welcome to Python member"

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
    
    return redirect(url_for('success',score=total_score))

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score<35:
        res= "The person result is Fail and the score is " + str(score)
    else:
        res= "The person result is Pass and the score is " + str(score)

    return render_template("result.html",result=res)



@app.route('/fail/<int:score>')
def fail(score):
    return "The person result is Fail and the score is " + str(score)



@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<35:
        result="fail"
    else:
        result="success"
    return redirect(url_for(result,score=marks))






if __name__=='__main__':
    app.run(debug=True)