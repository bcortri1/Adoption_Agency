from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

species_list = ["Dog", "Cat", "Porcupine", "Crab", "Rabbit"]

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet name",validators=[InputRequired()])
    species = StringField("Species",validators=[InputRequired(), AnyOf(species_list)])
    photo_url = StringField("Photo URL",validators=[Optional(), URL()])
    age = IntegerField("Age",validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes",validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing existing pets."""
    name = StringField("Pet name", render_kw={'readonly': True})
    species = StringField("Species", render_kw={'readonly': True})
    photo_url = StringField("Photo URL",validators=[Optional(), URL()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0, max=30)])
    notes = StringField("Notes",validators=[Optional()])
    available = BooleanField("Available",validators=[Optional()])