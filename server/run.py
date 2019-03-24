from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'


@app.route('/', methods=['GET'])
def run():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts=data)
# return jsonify({
    # 'status': 'ok',
    # 'message': 'API - thaymerPortillo 2019'})


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s,%s,%s)',
                    (fullname, phone, email))
        mysql.connection.commit()
        flash('Contacto Agregado')
        return redirect(url_for('run'))


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    print(data[0])
    return render_template('edit-contacts.html', contact=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE contacts
    SET fullname = %s,
        phone = %s,
        email = %s 
    WHERE id = %s
    """, (fullname, phone, email, id))
    mysql.connection.commit()
    flash('Contacto Editado')
    return redirect(url_for('run'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('run'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
