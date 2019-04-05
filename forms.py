from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):

    ancestry = SelectField('Ancestry', validators=[DataRequired], choices=[
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

    experience = SelectField('Experience', validators=[DataRequired], choices=[
        ('Green', 'Green'),
        ('Regular', 'Regular'),
        ('Seasoned', 'Seasoned'),
        ('Veteran', 'Veteran'),
        ('Elite', 'Elite'),
        ('Super Elite', 'Super Elite')
    ])

    equipment = SelectField('Equipment', validators=[DataRequired], choices=[
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('Heavy', 'Heavy'),
        ('Super Heavy', 'Super Heavy'),
    ])

    unit_type = SelectField('Unit Type', validators=[DataRequired], choices=[
        ('Flying', 'Flying'),
        ('Archers', 'Archers'),
        ('Calvary', 'Calvary'),
        ('Levies', 'Levies'),
        ('Infantry', 'Infantry'),
        ('Siege Engine', 'Siege Engine')
    ])

    unit_size = SelectField('Unit Size', validators=[DataRequired], choices=[
        ('1d4', '1d4'),
        ('1d6', '1d6'),
        ('1d8', '1d8'),
        ('1d10', '1d10'),
        ('1d12', '1d12')
    ])

    submit_button = SubmitField('Submit')
