from flask import Flask,render_template,request
import sqlite3 as sq


app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/form">Form</a>'


@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        city = request.form['city']
        email = request.form['email']
        num = request.form['num']
        con = sq.connect("datamine.db")
        cur = con.cursor()
        cur.execute('''insert into student_details values(?,?,?,?)''',(name,city,email,num))
        con.commit()
        con.close()

    return render_template('form.html')


if __name__== '__main__':
    app.run(debug=True)
