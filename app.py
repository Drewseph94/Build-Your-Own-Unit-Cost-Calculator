from flask import Flask, render_template, request
from forms import CalculatorForm
import CostCalculation

app = Flask(__name__)
app.config['SECRET_KEY'] = '53b102d4c540e444152a068e3ae5b9ce'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    return render_template('build-your-own-unit.html', form=form, total_cost=0, token=app.config['SECRET_KEY'])

@app.route('/calculate', methods=['POST'])
def calculate():
    result = request.form
    print(result['attack_bonus'])
    total_cost = CostCalculation.calculate_cost(
        result['attack_bonus'],
        result['power_bonus'],
        result['defense_bonus'],
        result['toughness_bonus'],
        result['morale_bonus'],
        result['unit_type'],
        result['unit_size'])
    form = CalculatorForm()
    return render_template('build-your-own-unit.html', form=form, total_cost=total_cost)

if __name__ == '__main__':
    app.run()
