from wtforms import Form, StringField, TextAreaField


class PostForms(Form):
    title = StringField('Title')
    body = TextAreaField('body')