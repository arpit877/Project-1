from flask import Flask,render_template,request

import sqlite3 as sql 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_customer():
    return render_template('customer.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            Id = request.form['ID']
            Name = request.form['nm']
            Email = request.form['mail']
            Subscription = request.form['sub']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO customer (id,name,email,subscription) VALUES (?,?,?,?)",(Id,Name,Email,Subscription))

                con.commit()

                msg = "Record Successfully Added"
            
        except:
            con.rollback()
            msg="error in insert operation"

        finally:
            return render_template("result.html",msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select*from customer")

    rows = cur.fetchall()

    return render_template("list.html",rows=rows)

if __name__ =='__main__':
    app.run(debug=True)