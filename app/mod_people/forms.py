from wtforms_alchemy import ModelForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms_alchemy.validators import Unique
from app.mod_people.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        strip_string_fields = True

    first_name = StringField(
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    last_name = StringField(
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    email = StringField(
        validators=[DataRequired(), Email(), Unique('email')]
    )

    phone = StringField(
        validators=[DataRequired(), Regexp('\d{9}')]
    )

    eid = StringField(
        validators=[DataRequired(), Regexp('\d{5}')]
    )

    gen = StringField(
        validators=[DataRequired(), Length(min=4, max=6)]
    )

    cls = StringField(
        validators=[DataRequired(), Length(min=4, max=8)]
    )

    Adr = StringField(
        validators=[DataRequired(), Length(min=5, max=50)]
    )

    bgr = StringField(
        validators=[DataRequired(), Length(min=2, max=4)]
    )

    fname = StringField(
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    mname = StringField(
        validators=[DataRequired(), Length(min=3, max=50)]
    )

    dob = StringField(
        validators=[DataRequired(), Length(min=3, max=50)]
    )