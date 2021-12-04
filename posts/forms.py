from wtforms import Form, StringField, TextAreaField


class PostForms(Form):
    title = StringField('Title', render_kw={'placeholder': 'Заголовок'})
    body = TextAreaField('Body', render_kw={'placeholder': 'Текст'})