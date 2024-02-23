import os, requests
from flask import Flask, render_template
from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'development key'

class MyForm(FlaskForm):
    rollno = StringField('Roll No :', validators=[DataRequired()])
    passw = PasswordField('Password :',validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route('/',methods=['GET','POST'])
def certificates():
    form = MyForm()
    backendurl=os.getenv("backendurl")
    error=[]
    if form.validate_on_submit():
        print("hihihi")
        
        print(form.rollno,form.passw.data)
        resp=requests.post(url=backendurl,params={"rno":form.rollno.data,"pass":form.passw.data})
        if resp.status_code==200:
            status,data=resp.json()
            print(resp.json())
            if status==True:
                return render_template("SV2.html",name=data[0],tabledata=render_template_string(data[1]))
            else:
                return render_template("certificates.html",form=form,errors=data)  
    return render_template('certificates.html',form=form,errors=error)


#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return render_template('index.html')
#    return render_template('submit.html', form=form)


