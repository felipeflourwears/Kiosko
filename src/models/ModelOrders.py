from .entities.Order import Order

class ModelOrders():

    @classmethod
    def get_orders_all_db(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%Y-%m-%d %H:%i:%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode ORDER BY o.idOrder DESC;"
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
    @classmethod
    def get_orders_pending_db(cls, db, offset, limit):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%%Y-%%m-%%d %%H:%%i:%%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode WHERE o.served <> 1 ORDER BY o.idOrder DESC LIMIT %s OFFSET %s;"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            orders = []

            for row in rows:
                order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                orders.append(order)

            return orders
        except Exception as ex:
            raise Exception(str(ex))
