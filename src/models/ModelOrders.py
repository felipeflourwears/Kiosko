from .entities.Order import Order
import math

class ModelOrders():

    def get_orders(self, db, request):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            page = 1

        variante = 6
        num_per_page = variante
        start_from = (page - 1) * variante

        cur = db.connection.cursor()
        cur.execute(f"SELECT idFood, f.nameFood, f.priceFood, f.imageUrl, f.descriptionFood, f.available, c.nameCategory FROM foodMenu f INNER JOIN categoryfood c ON f.idCategory = c.idCategory ORDER BY f.idFood DESC LIMIT {start_from}, {num_per_page}")
        result = cur.fetchall()

        cur.execute("SELECT idFood, f.nameFood, f.priceFood, f.imageUrl, f.descriptionFood, f.available, c.nameCategory FROM foodMenu f INNER JOIN categoryfood c ON f.idCategory = c.idCategory ORDER BY f.idFood DESC")
        total_record = cur.rowcount

        total_page = math.ceil(total_record / num_per_page)

        cur.close()

        start_range = max(1, page - 2)
        end_range = min(total_page, page + 2)

        return (result, page, total_page, start_range, end_range)

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
