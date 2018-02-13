from model import InputForm
from flask import Flask, render_template, request
from compute import compute
import sys

import random
import io
import matplotlib.pyplot as plt
import base64

from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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


@app.route('/template', methods=['GET', 'POST'])
def template():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                           form.w.data, form.T.data)

    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/plot')
def build_plot():
    img = io.BytesIO()

    y = [1, 2, 3, 4, 5]
    x = [0, 2, 1, 3, 4]
    plt.plot(x, y)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)


@app.route('/main')
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
