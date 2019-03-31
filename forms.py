from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):
    attack_bonus = IntegerField('Attack Bonus', validators=[DataRequired()])
    power_bonus = IntegerField('Power Bonus', validators=[DataRequired()])
    defense_bonus = IntegerField('Defense Bonus', validators=[DataRequired()])
    toughness_bonus = IntegerField('Toughness Bonus', validators=[DataRequired()])
    morale_bonus = IntegerField('Morale Bonus', validators=[DataRequired()])

    unit_size = SelectField('Unit Size', choices=[(4, '1d4'), (6, '1d6'), (8, '1d8'), (10, '1d10'), (12, '1d12')],
                           validators=[DataRequired()])
    unit_type = SelectField('Unit Type', choices=[
                                            ('Levy', 'Levy'),
                                            ('Infantry', 'Infantry'),
                                            ('Calvary', 'Calvary'),
                                            ('Siege Engine', 'Siege Engine'),
                                            ('Archer', 'Archer'),
                                            ('Flying', 'Flying')
                                        ],
                           validators=[DataRequired()])

    submit_button = SubmitField('Submit')
