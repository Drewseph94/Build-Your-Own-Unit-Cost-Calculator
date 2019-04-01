from flask import Flask, render_template, request
from forms import CalculatorForm
import CostCalculation
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
    ancestry = Unit.Ancestry(submission['ancestry'])
    experience = Unit.Experience(submission['experience'])
    equipment = Unit.Equipment(submission['equipment'])
    unit_type = Unit.Type(submission['unit_type'])
    unit_size = Unit.Size(submission['unit_size'])
    unit = Unit.Unit(ancestry,experience,equipment,unit_type,unit_size)
    total_cost = CostCalculation.calculate_cost(unit)
    # total_cost = CostCalculation.calculate_cost(
    #     result['attack_bonus'],
    #     result['power_bonus'],
    #     result['defense_bonus'],
    #     result['toughness_bonus'],
    #     result['morale_bonus'],
    #     result['unit_type'],
    #     result['unit_size'])
    form = CalculatorForm()
    return render_template('build-your-own-unit.html', form=form, total_cost=0)

if __name__ == '__main__':
    app.run()
