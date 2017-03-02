from wtforms import StringField
from flask_security.forms import RegisterForm,ConfirmRegisterForm

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username',[])


class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
    username = StringField('Username',[])
    nickname = StringField('Nickname',[])
