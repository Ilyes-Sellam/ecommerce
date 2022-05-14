from wtforms import StringField, FloatField, BooleanField, SelectField, SubmitField, Form, FormField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

from shop.models import Categorie


# class CategorieForm(Form):
#     categorie_name = StringField('Categorie')

class CreateProduct(FlaskForm):
    product_name = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=200)])
    product_price = FloatField('Product Price',
                        validators=[DataRequired()])
    image_path = FileField('Upload The product image', validators=[
                        FileAllowed(['jpg', 'png'])])
    product_size = StringField('Product Size',
                           validators=[DataRequired(), Length(min=1, max=4)])
    product_description = StringField('Product Description',
                           validators=[DataRequired(), Length(min=2, max=200)])
    available = BooleanField('Available',
                           validators=[DataRequired()])
    categories = Categorie.query.all()
    categorie = SelectField('Category', choices=[(cat.id, cat.categorie_name) for cat in categories], validators=[DataRequired()])
    # categories = FieldList(FormField(CategorieForm), min_entries=4, max_entries=8)

    submit = SubmitField('Add Product')
