from flask import Flask, render_template, request
from forms import CalculatorForm
import CostCalculation
import Unit

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b102d4c540e444152a068e3ae5b9ce'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    return render_template('build-your-own-unit.html', form=form, total_cost=0, token=app.config['SECRET_KEY'])


@app.route('/calculate', methods=['POST'])
def calculate():
    submission = request.form
    form = CalculatorForm()

    ancestry = Unit.Ancestry(submission['ancestry'])
    experience = Unit.Experience(submission['experience'])
    equipment = Unit.Equipment(submission['equipment'])
    unit_type = Unit.Type(submission['unit_type'])
    unit_size = Unit.Size(submission['unit_size'])

    unit = Unit.Unit(ancestry, experience, equipment, unit_type, unit_size)
    total_cost = CostCalculation.calculate_cost(unit)

    return render_template('build-your-own-unit.html', form=form, total_cost=total_cost)


if __name__ == '__main__':
    app.run()
    app.config['SERVER_NAME'] = 'http://drewseph94.pythonanywhere.com/'
