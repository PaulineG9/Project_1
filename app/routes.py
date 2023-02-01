from flask import Flask ,render_template,url_for, request, flash, redirect

import os
from os import environ

import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 


from app import app


# read MailerToGo env vars
mailertogo_host     = environ.get('MAILERTOGO_SMTP_HOST')
mailertogo_port     = environ.get('MAILERTOGO_SMTP_PORT', 587)
mailertogo_user     = environ.get('MAILERTOGO_SMTP_USER')
mailertogo_password = environ.get('MAILERTOGO_SMTP_PASSWORD')
mailertogo_domain   = environ.get('MAILERTOGO_DOMAIN', "www.paulineg.dev")


sender_user = 'noreply'
sender_email = "@".join([sender_user, mailertogo_domain])
sender_name = 'Pauline G'

# recipient
recipient_email = sender_email # change to recipient email. Make sure to use a real email address in your tests to avoid hard bounces and protect your reputation as a sender.
recipient_name = 'Ms. PaulineG'



@app.route('/')
@app.route('/index',  methods=['POST'])
def index():
        return render_template("index.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():


        if request.method == 'POST':

                result= {}

                result['name'] = request.form['name']
                result['email'] = request.form['email']
                result['subject'] = request.form['message']

                message =  """
                
                You just received a contact form.

                Name: {}
                Email: {}
                \n\n
                Message: {}

                

                
                """.format(result['name'],result['email'],result['subject'])

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login( os.getenv("MAIL_USERNAME") ,os.getenv("MAIL_PASSWORD"))
                # server.login(mailertogo_user, mailertogo_password)
                server.sendmail(result['email'], os.getenv("MAIL_DEFAULT_SENDER"), message)
                # server.sendmail(sender_email, recipient_email, message)
                server.close()


        return render_template('index.html', success = True)


@app.route('/projects')
def projects():
        return render_template("projects.html")


@app.route('/resume')
def resume():
        return render_template("resume.html")


@app.route('/wadish')
def wadish():
        return render_template("wadish2022.html")

@app.route('/wadish2')
def wadish2():
        return render_template("wadish2021.html")


if __name__ == "__main__":
        app.run(debug=True)




