from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOEmpleados import DAOEmpleados
from dao.DAOObservaciones import DAOObservaciones



app = Flask(__name__)
app.secret_key = "Ut3c_123456" #texto super largo 

db = DAOUsuario()
db_empleados = DAOEmpleados()
db_observaciones = DAOObservaciones()



@app.route('/')   #root route
def inicio():
#    return "UTEC - rosario quispe"
    return render_template('index.html')




@app.route('/usuario/')  
def index():
    datos = db.read(None)
    return render_template('usuario/index.html', data=datos)


@app.route('/usuario/add/')
def add():
    return render_template('/usuario/add.html')

@app.route('/usuario/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/usuario/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route('/usuario/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/usuario/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route('/usuario/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# ----------------------------------------------------------------
@app.route('/login')
def loginPage():
    return render_template('login.html', title='Login Page')
 
@app.route('/about')
def aboutPage():
    return render_template('about.html', title='About')


# ----------------------------------------------------------------

@app.route('/empleados/')  
def index_empleados():
    datos_empleados = db_empleados.read(None)  # 
    return render_template('empleados/index.html', data_empleados=datos_empleados)


@app.route('/empleados/add/')
def add_empleados():
    return render_template('/empleados/add.html')

@app.route('/empleados/addempleados', methods = ['POST', 'GET'])
def addempleados():
    if request.method == 'POST' and request.form['save']:
        if db_empleados.insert(request.form):
            flash("Nuevo empleados creado")
        else:
            flash("ERROR, al crear empleados")

        return redirect(url_for('index_empleados'))
    else:
        return redirect(url_for('index_empleados'))

@app.route('/empleados/update/<int:id>/')
def update_empleados(id):
    data_empleados = db_empleados.read(id);

    if len(data_empleados) == 0:
        return redirect(url_for('index_empleados'))
    else:
        session['update'] = id
        return render_template('empleados/update.html', data_empleados = data_empleados)

@app.route('/empleados/updateempleados', methods = ['POST'])
def updateempleados():
    if request.method == 'POST' and request.form['update']:

        if db_empleados.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index_empleados'))
    else:
        return redirect(url_for('index_empleados'))

@app.route('/empleados/delete/<int:id>/')
def delete_empleados(id):
    data_empleados = db_empleados.read(id);

    if len(data_empleados) == 0:
        return redirect(url_for('index_empleados'))
    else:
        session['delete'] = id
        return render_template('empleados/delete.html', data_empleados = data_empleados)

@app.route('/empleados/deleteempleados', methods = ['POST'])
def deleteempleados():
    if request.method == 'POST' and request.form['delete']:

        if db_empleados.delete(session['delete']):
            flash('empleados eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index_empleados'))
    else:
        return redirect(url_for('index_empleados'))


#-------------------------------------------------------------------------

@app.route('/observaciones/')  
def index_observaciones():
    datos_observaciones = db_observaciones.read(None)  # 
    return render_template('observaciones/index.html', data_observaciones=datos_observaciones)








if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0",debug=True)  #port 5000 por defecto 

