from flask import Flask
from flask import render_template
from flask import request
from StringCounter import StringCounter

app = Flask(__name__)
candidates = StringCounter()


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def homepage():
    print(request.form)
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            candidates.count(request.form['input'])
        else:
            pass



    return render_template('index.html',
            candidates=candidates)

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        if request.form['submit'] == 'Clear':
            candidates.clear()
    return render_template('results.html',
            candidates = candidates)

if __name__ == '__main__':
    app.run(debug=True)
