from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import config
from flask_mysqldb import MySQL

#Import to manage tokens to authenticate
from flask_wtf.csrf import CSRFProtect

#Import to manage control with LOGIN
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

#Models
from models.ModelUser import ModelUser
from models.ModelOrders import ModelOrders

#Entities
from models.entities.User import User
from models.entities.Order import Order

#Instances
csrf = CSRFProtect()
app = Flask(__name__)
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    current_user_mode = 0  # Establecer el modo predeterminado en 0 si no se encuentra ningún usuario

    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'], 0, 0)
        logged_user = ModelUser.login(db, user)
        if logged_user:
            current_user_mode = logged_user.mode  # Actualizar el valor de current_user_mode si se encuentra un usuario
            print("MODE: ", current_user_mode)
            print("IDROL: ", logged_user.idRol)
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid Password...")
        else:
            flash("User not found...")
    return render_template('auth/login.html', current_user_mode=current_user_mode)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html', current_page="home")

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida solo para usuarios autenticados</h1>"

@app.route('/get_orders_pending')
def get_orders_pending():
    try:
        orders = ModelOrders.get_orders_pending_db(db)  # Llama a la función para obtener datos de pedidos
        # Convierte los datos de pedidos en un formato adecuado (por ejemplo, una lista de diccionarios)
        data = [{'table': order.nameTable, 'nameFood': order.nameFood, 'quantity': order.quantity, 'description': order.descriptionOrd, 'date': order.dateDay, 'total': order.total, 'served': order.served} for order in orders]
        return jsonify(data)
    except Exception as ex:
        return jsonify({'error': str(ex)})

@app.route('/get_orders_all')
def get_orders_all():
    try:
        orders = ModelOrders.get_orders_all_db(db)  # Llama a la función para obtener datos de pedidos
        # Convierte los datos de pedidos en un formato adecuado (por ejemplo, una lista de diccionarios)
        data = [{'table': order.nameTable, 'nameFood': order.nameFood, 'quantity': order.quantity, 'description': order.descriptionOrd, 'date': order.dateDay, 'total': order.total, 'served': order.served} for order in orders]
        return jsonify(data)
    except Exception as ex:
        return jsonify({'error': str(ex)})
    
@app.route('/products')
@login_required
def products():
    return render_template('products.html', current_page='products')

@app.route('/orders')
@login_required
def orders():
    return render_template('orders.html', current_page='orders')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return render_template("404.html")

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
