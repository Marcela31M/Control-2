from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length
from models.user import User


class OrderCreateForm(FlaskForm):
    buyer = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "buyer"},
    )

    tax = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "tax"},
    )

    discount = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "discount"},
    )

    submit = SubmitField("create")
