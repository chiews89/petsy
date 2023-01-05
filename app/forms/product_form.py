from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()] )
    image_url = StringField('Image', validators=[DataRequired()], )
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()] )
    category_id = IntegerField('Category', validators=[DataRequired()])
