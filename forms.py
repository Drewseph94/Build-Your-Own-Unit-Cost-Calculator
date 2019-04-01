from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):
    # attack_bonus = IntegerField('Attack Bonus', validators=[DataRequired()])
    # power_bonus = IntegerField('Power Bonus', validators=[DataRequired()])
    # defense_bonus = IntegerField('Defense Bonus', validators=[DataRequired()])
    # toughness_bonus = IntegerField('Toughness Bonus', validators=[DataRequired()])
    # morale_bonus = IntegerField('Morale Bonus', validators=[DataRequired()])
    #
    # unit_size = SelectField('Unit Size', choices=[('d4', '1d4'), ('d6', '1d6'), ('d8', '1d8'), ('d10', '1d10'), ('d12', '1d12')],
    #                        validators=[DataRequired()])
    # unit_type = SelectField('Unit Type', choices=[
    #                                         ('Levy', 'Levy'),
    #                                         ('Infantry', 'Infantry'),
    #                                         ('Calvary', 'Calvary'),
    #                                         ('Siege Engine', 'Siege Engine'),
    #                                         ('Archer', 'Archer'),
    #                                         ('Flying', 'Flying')
    #                                     ],
    #                        validators=[DataRequired()])
    #
    # submit_button = SubmitField('Submit')

    ancestry = SelectField('Ancestry', choices=[
        ('Bugbear', 'Bugbear'),
        ('Dragonborn', 'Dragonborn'),
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Elf (Winged)', 'Elf (Winged)'),
        ('Ghoul', 'Ghoul'),
        ('Gnoll', 'Ghoul'),
        ('Gnome', 'Gnome'),
        ('Goblin', 'Goblin'),
        ('Hobgoblin', 'Hobgoblin'),
        ('Human', 'Human'),
        ('Kobold', 'Kobold'),
        ('Lizardfolk', 'Lizardfolk'),
        ('Ogre', 'Orc'),
        ('Orc', 'Orc'),
        ('Skeleton', 'Skeleton'),
        ('Treant', 'Treant'),
        ('Troll', 'Troll'),
        ('Zombie', 'Zombie')
    ])

    experience = SelectField('Experience', choices=[
        ('Green', 'Green'),
        ('Regular', 'Regular'),
        ('Seasoned', 'Seasoned'),
        ('Veteran', 'Veteran'),
        ('Elite', 'Elite'),
        ('Super Elite', 'Super Elite')
    ])

    equipment = SelectField('Equipment', choices=[
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('Heavy', 'Heavy'),
        ('Super Heavy', 'Super Heavy'),
    ])

    unit_type = SelectField('Unit Type', choices=[
        ('Flying', 'Flying'),
        ('Archers', 'Archers'),
        ('Calvary', 'Calvary'),
        ('Levies', 'Levies'),
        ('Infantry', 'Infantry'),
        ('Siege Engine', 'Siege Engine')
    ])

    unit_size = SelectField('Unit Size', choices=[
        ('1d4', '1d4'),
        ('1d6', '1d6'),
        ('1d8', '1d8'),
        ('1d10', '1d10'),
        ('1d12', '1d12')
    ])

    submit_button = SubmitField('Submit')
