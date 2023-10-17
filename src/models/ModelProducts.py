import math

class ModelProducts:
    def get_products(self, db, request, search=None):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            page = 1

        variante = 6
        num_per_page = variante
        start_from = (page - 1) * variante

        search_query = ''
        if search:
            search_query = f"AND f.nameFood LIKE '%{search}%'"

        cur = db.connection.cursor()
        cur.execute(f"SELECT idFood, f.nameFood, f.priceFood, f.imageUrl, f.descriptionFood, f.available, c.nameCategory FROM foodMenu f INNER JOIN categoryfood c ON f.idCategory = c.idCategory WHERE 1 {search_query} ORDER BY f.idFood DESC LIMIT {start_from}, {num_per_page}")
        result = cur.fetchall()

        cur.execute(f"SELECT idFood, f.nameFood, f.priceFood, f.imageUrl, f.descriptionFood, f.available, c.nameCategory FROM foodMenu f INNER JOIN categoryfood c ON f.idCategory = c.idCategory WHERE 1 {search_query} ORDER BY f.idFood DESC")
        total_record = cur.rowcount

        total_page = math.ceil(total_record / num_per_page)

        cur.close()

        start_range = max(1, page - 2)
        end_range = min(total_page, page + 2)

        return (result, page, total_page, start_range, end_range)