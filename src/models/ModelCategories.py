import math

class ModelCategories:
    def get_categories(self, db):
        cur = db.connection.cursor()
        cur.execute("SELECT idCategory, nameCategory FROM categoryFood")
        categories = cur.fetchall()
        cur.close()
        return categories
    
    def get_categories_table(self, db, request, search=None):
        if 'page' in request.args:
            page = int(request.args['page'])
        else:
            page = 1
        variante = 6
        num_per_page = variante
        start_from = (page - 1) * variante

        search_query = ''
        params = []

        if search and search.lower() != 'none':
            search_query = " AND c.nameCategory LIKE %s "
            params.append(f"%{search}%")

        cur = db.connection.cursor()
        cur.execute(f"SELECT c.idCategory, c.nameCategory FROM categoryFood c WHERE 1 {search_query} ORDER BY c.idCategory DESC LIMIT {start_from}, {num_per_page}", params)
        result = cur.fetchall()

        cur.execute(f"SELECT c.idCategory, c.nameCategory FROM categoryFood c WHERE 1 {search_query}", params)
        total_record = cur.rowcount

        total_page = math.ceil(total_record / num_per_page)

        cur.close()

        start_range = max(1, page - 2)
        end_range = min(total_page, page + 2)

        return (result, page, total_page, start_range, end_range)
    
    def add_category(self, db, name_category):
        cur = db.connection.cursor()
        cur.execute("INSERT INTO categoryFood (nameCategory) VALUES (%s)", (name_category,))
        db.connection.commit()
        cur.close()
