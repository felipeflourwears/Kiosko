from .entities.Order import Order
import math

class ModelOrders():

    def get_orders(self, db, request, search=None):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            page = 1
        variante = 15
        num_per_page = variante
        start_from = (page - 1) * variante

        search_query = ''
        if search:
            search_query = f"AND c.numberTable LIKE '%{search}%'"

        cur = db.connection.cursor()
        #SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%Y-%m-%d %H:%i:%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode ORDER BY o.idOrder DESC LIMIT 0 , 2;
        cur.execute(f"SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%Y-%m-%d %H:%i:%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode WHERE 1 {search_query} ORDER BY o.idOrder, o.dateDay DESC LIMIT {start_from}, {num_per_page}")
        result = cur.fetchall()

        cur.execute(f"SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%Y-%m-%d %H:%i:%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode WHERE 1 {search_query} ORDER BY o.idOrder DESC")
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
            sql = "SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%Y-%m-%d %H:%i:%s') as formatted_date, o.total, o.served, o.idOrder FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode WHERE o.served <> 1 ORDER BY o.idOrder DESC;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            orders = [] 

            for row in rows:
                # Crea objetos de pedido (Order) con los datos obtenidos
                order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                orders.append(order)

            return orders
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_orders_pending_db(cls, db, offset, limit):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT c.numberTable, f.nameFood, o.quantity, o.descriptionOrd, DATE_FORMAT(o.dateDay, '%%Y-%%m-%%d %%H:%%i:%%s') as formatted_date, o.total, o.served FROM orders o INNER JOIN foodmenu f ON o.idFood = f.idFood INNER JOIN client c ON c.userCode = o.userCode WHERE o.served = 0 ORDER BY o.idOrder DESC LIMIT %s OFFSET %s;"
            cursor.execute(sql, (limit, offset))
            rows = cursor.fetchall()
            orders = []

            for row in rows:
                order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                orders.append(order)

            return orders
        except Exception as ex:
            raise Exception(str(ex))
      
    @classmethod  
    def update_order(self, db, idOrder):
        cur = db.connection.cursor()
        cur.execute("UPDATE orders SET served = 1 WHERE idOrder = %s", (idOrder,))
        db.connection.commit()
        cur.close()
        return "Order updated successfully"