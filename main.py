import requests
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import time
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Api requests
headers = {
    "Authorization": "Bearer 0-GlZyKRIHcbz9fb9-5j"
}
time.sleep(1)
response = requests.get(url="https://the-one-api.dev/v2/character", headers=headers)
print(response.status_code)
data = response.json()


def get_info(name):
    for item in data['docs']:
        if item['name'].lower() == name.lower():
            return item


time.sleep(5)
response2 = requests.get(url="https://the-one-api.dev/v2/quote", headers=headers)
print(response2.status_code)
quote_data = response2.json()


# Flask forms
class NameForm(FlaskForm):
    name = StringField('Enter a character name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class QuoteForm(FlaskForm):
    submit = SubmitField('Get a random LoTR Quote')


@app.route("/", methods=["GET", "POST"])
def home():
    form = NameForm()
    form_2 = QuoteForm()
    if form.validate_on_submit():
        # get details of name
        character_name = form.name.data
        dictionary = get_info(character_name)
        # pass the value to index.html
        return render_template("char.html", data=dictionary)

    if form_2.validate_on_submit():
        random_no = randint(0, 920)
        quote = quote_data['docs'][random_no]
        return render_template("quote.html", data=quote)
    return render_template("index.html", form=form, form_q=form_2)


if __name__ == '__main__':
    app.run(debug=True)
