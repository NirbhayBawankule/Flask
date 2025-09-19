from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><body><h1>Welcome!!</h1></body></html>"+"Nice to meet you!"

@app.route("/pass/<int:score")
def passed(score):
    return "<html><body><h1>Passed!!</h1></body></html>"+"You passed by " + str(score)

@app.route("/fail/<int:score")
def failed(score):
    return "<html><body><h1>Failed!!</h1></body></html>"+"You failed by " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if makrs<40:
        result = "fail"
    else:
        result = "pass"
    return redirect(url_for(result,score = marks))



if __name__=='__main__':
    app.run(debug==True)