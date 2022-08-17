import mysql.connector as sql
import json
from flask import Flask, jsonify, make_response, redirect, render_template, request


#establishing connection with mySQL database
connection = sql.connect(host='sql6.freemysqlhosting.net', user='sql6513340', password='Iluqh1ZCX3', database='sql6513340')
c = connection.cursor()



app = Flask(__name__)



@app.errorhandler(403)
def error_403(e):
    return render_template('/error404.html', error = "403")

@app.errorhandler(404)
def error_404(e):
    return render_template('/error404.html', error = "404")


@app.errorhandler(500)
def error_500(e):
    return render_template('/error404.html', error = "500")



@app.route('/students/<city>', methods=['GET'])
def students(city):
    #return "welcome to city : {}".format(city)
    f=open('./data/{}/students.json'.format(city), "rb")
    content = json.load(f)
    f.close()
    s = 'returned from server no. 3<br><br><br>'
    for i in content:
        s += str(i) + '<br>'
    return s
    #return render_template('display.html', jsonfile=content)


@app.route('/faculty/<city>', methods=['GET'])
def faculty(city):
    #return "welcome to city : {}".format(city)
    f=open('./data/{}/faculty.json'.format(city), "rb")
    content = json.load(f)
    f.close()
    s = 'returned from server no. 3<br><br><br>'
    for i in content:
        s += str(i) + '<br>'
    return s
    #return render_template('display.html', jsonfile=content)


@app.route('/interests', methods=['GET', 'POST'])
def interests():
    if request.method == "GET":
        return render_template('interests.html')
    if request.method == "POST":
        username = str(request.form.get('username'))
        interests = str(request.form.get('interests'))
        c.execute('INSERT INTO TABLE interests(username, interests) VALUES({}, {})'.format(username, interests))
        connection.commit()
        return "Thank you for letting us know about your interest, {}.".format(username)

    

   
if __name__ == '__main__':
    app.run(port='8083')