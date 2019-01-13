from wtforms import Form, BooleanField, StringField, validators, IntegerField, SelectField

class RegistrationForm(Form):
    name = StringField('Name:', [validators.Length(min=4, max=25)])
    age = IntegerField('Age:', [validators.number_range(min=6, max=100)])
    gender = SelectField('Gender:', choices=[('f', 'Female'), ('m', 'Male')])
    height = IntegerField('Height (in cm):', [validators.number_range(min=100, max=250)])
    weight = IntegerField('Weight (in kg):', [validators.number_range(min=20, max=300)])
    diet = SelectField('Diet:', choices=[('balanced', 'Balanced'), ('slight', 'Slightly Unhealthy'), ('unhealthy', 'Unhealthy')])
