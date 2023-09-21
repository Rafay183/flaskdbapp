from flask import Flask, request, render_template
from flask_mysqldb import MySQL


app=Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Lmnopqrst1234+'
app.config['MYSQL_DB']='mydb'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():


    if request.method == 'GET':
        return "Login via login form"


    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO users (name,email) VALUES(%s , %s)''',(username,email))
        mysql.connection.commit()
        cur.close()
        return 'Successfully updated record in database'
    return render_template("index.html")

@app.route("/users")
def getusers():
    cur = mysql.connection.cursor()
    user_rec=cur.execute('SELECT * from users')
    if user_rec > 0:
        userDetails = cur.fetchall()
    return render_template('users.html',users=userDetails)

if __name__ == "__main__":
    app.run(debug=True)