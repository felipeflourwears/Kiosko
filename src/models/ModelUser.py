from .entities.User import User
from .entities.Order import Order

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod   
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_orders_db(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, o.dateDay, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.idClient = o.idClient ORDER BY o.idOrder DESC"
            cursor.execute(sql)
            rows = cursor.fetchall()
            orders = []

            for row in rows:
                # Crea objetos de pedido (Order) con los datos obtenidos
                order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                orders.append(order)

            return orders
        except Exception as ex:
            raise Exception(ex)