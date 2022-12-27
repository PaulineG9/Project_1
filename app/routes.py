from flask import Flask ,render_template,url_for, request, flash, redirect
import smtplib



from app import app

import os



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
                server.starttls()
                server.login( os.getenv("MAIL_USERNAME") ,os.getenv("MAIL_PASSWORD"))
                server.sendmail(result['email'], os.getenv("MAIL_DEFAULT_SENDER"), message)


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




