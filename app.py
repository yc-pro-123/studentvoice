from flask import Flask, render_template
from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'development key'

class MyForm(FlaskForm):
    rollno = StringField('Roll No :', validators=[DataRequired()])
    passw = IntegerField('Password :',validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route('/',methods=['GET','POST'])
def certificates():
    form = MyForm()
    if form.validate_on_submit():
        print("hihihi")
        print(form.rollno,form.passw.data)
        #return_template('certificates.html',form=hehe)
        pass
    return render_template('certificates.html',form=form)


#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return render_template('index.html')
#    return render_template('submit.html', form=form)


if __name__ == '__main__':
   app.run(debug = True)