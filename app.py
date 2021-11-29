from flask import Flask
from flask import render_template, request 

#aqui se relaciona python con la Base de datos creada
from flaskext.mysql import MySQL #importamos la libreria de base de datos que tiene flask

app = Flask(__name__)

mysql = MySQL() #se crea un nuevo objeto de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #se configura la base de datos
app.config['MYSQL_DATABASE_USER'] = 'root' #se cambia el usuario de xampp (el servidor)
app.config['MYSQL_DATABASE_PASSWORD'] = '' #en este caso, nada, porque no se cambió
app.config['MYSQL_DATABASE_DB'] = 'sistema2171'
mysql.init_app(app) #esta configuración se googlea, no hay que memorizarla




#relacionamos el html con Python
@app.route('/') #especifica donde entra en el controlador
def index(): #esta funcion va a insertar en la base de datos, los registros que se les pase
    sql= "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'tuki', 'tukicapo@gmail.com', 'fotodetuki.jpg')" #se copia del registro de xampp
    conn=mysql.connect() #abro la conexion 
    cursor=conn.cursor() #creo el cursor
    cursor.execute(sql) #ejecuto el cursor
    conn.commit() #abro el commit, lo mando a la base de datos
    return render_template('empleados/index.html') 

@app.route('/create')
def create():
    return render_template('empleados/create.html') 

@app.route('/store', methods=['POST']) #esto sería para almacenar los registros ingresados
def storage():
    _nombre=request.form['txtNombre'] #viene del modulo request que importamos
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto'] #se llaman variables para que sea más cómodo
    

    sql= "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
    datos=(_nombre,_correo,_foto.filename)

    conn=mysql.connect() #abro la conexion 
    cursor=conn.cursor() #creo el cursor
    cursor.execute(sql,datos) #ejecuto el cursor
    conn.commit() #abro el commit, lo mando a la base de datos
    return render_template('empleados/index.html') 


if __name__=='__main__':
    app.run(debug=True)
