from flask import Flask, render_template
from forms import CalculatorForm
import CalculateCost

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b102d4c540e444152a068e3ae5b9ce'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    return render_template('build-your-own-unit.html', form=form, token=app.config['SECRET_KEY'])


if __name__ == '__main__':
    app.run()
