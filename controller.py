from model import InputForm
from flask import Flask, render_template, request
from compute import compute
import sys

app = Flask(__name__)

# try:
#     template_name = sys.argv[1]
# except IndexError:
#     template_name = 'view_plain'
#
# if template_name == 'view_flask_bootstrap':
#     from flask_bootstrap import Bootstrap
#
#     Bootstrap(app)


@app.route('/vib1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/hello")
def hello():
    return render_template('hello.html')


@app.route("/sample")
def sample():
    return render_template('sample.html')


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getMember(name):
    return name


if __name__ == '__main__':
    app.run(debug=True)
