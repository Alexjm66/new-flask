from flask import render_template,  Flask, request
import smtplib

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route('/about/')
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html')

@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html',name=name)
@app.route('/Send-email/', methods=['POST'])

def send_email():
    s_name = request.form['sender']
    s_password = request.form['password']
    sub= request.form['subject']
    message= request.form['message']

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        user=s_name
        receiver='maartalexander985@gmail.com '
        s.starttls()

        s.login(user,s_password)
        s.sendmail(user,receiver,sub,message)

        s.quit()
    except:
        print('You have an error')

    return 'Email sent'
