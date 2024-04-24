from wtforms import Form, StringField, PasswordField, validators, EmailField


class CreateAccountForm (Form):
    username = StringField('username', [validators.DataRequired("Username required")])
    email = EmailField('email', [validators.DataRequired(), validators.Email("Email required")])
    password = PasswordField('password', [validators.DataRequired("Password required"), validators.EqualTo("cpassword", "Not the same"), validators.Length(3, message="Password too short")])
    cpassword = PasswordField('confirm password', [validators.DataRequired("Confirm required")])
