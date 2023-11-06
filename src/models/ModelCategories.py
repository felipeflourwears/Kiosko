import math

class ModelCategories:
    def get_categories(self, db):
        try:
            with db.connection.cursor() as cur:
                query = "SELECT idCategory, nameCategory FROM categoryFood"
                cur.execute(query)
                categories = cur.fetchall()
                return categories
        except Exception as e:
            # Manejo de excepciones
            print(f"Error: {e}")
            return []

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

        try:
            with db.connection.cursor() as cur:
                query = f"SELECT c.idCategory, c.nameCategory FROM categoryFood c WHERE 1 {search_query} ORDER BY c.idCategory DESC LIMIT %s, %s"
                cur.execute(query, params + [start_from, num_per_page])
                result = cur.fetchall()

                cur.execute(f"SELECT c.idCategory, c.nameCategory FROM categoryFood c WHERE 1 {search_query}", params)
                total_record = cur.rowcount

                total_page = math.ceil(total_record / num_per_page)

                start_range = max(1, page - 2)
                end_range = min(total_page, page + 2)

                return (result, page, total_page, start_range, end_range)
        except Exception as e:
            # Manejo de excepciones
            print(f"Error: {e}")
            return ([], 1, 0, 1, 1)

    
    def add_category(self, db, name_category):
        try:
            with db.connection.cursor() as cur:
                query = "INSERT INTO categoryFood (nameCategory) VALUES (%s)"
                cur.execute(query, (name_category,))
                db.connection.commit()
        except Exception as e:
            # Manejo de excepciones
            print(f"Error: {e}")


    def delete_category(self, db, category_id):
        try:
            with db.connection.cursor() as cur:
                query = "DELETE FROM categoryFood WHERE idCategory = %s"
                cur.execute(query, (category_id,))
                db.connection.commit()
        except Exception as e:
            # Manejo de excepciones
            print(f"Error: {e}")


    def get_category_by_id(self, db, category_id):
        cur = db.connection.cursor()
        cur.execute("SELECT idCategory, nameCategory FROM categoryFood WHERE idCategory = %s", (category_id,))
        category = cur.fetchone()
        cur.close()
        return category
    
    def update_category(self, db, category_id, name_category):
        try:
            with db.connection.cursor() as cur:
                query = "UPDATE categoryFood SET nameCategory = %s WHERE idCategory = %s"
                cur.execute(query, (name_category, category_id))
                db.connection.commit()
        except Exception as e:
            # Manejo de excepciones
            print(f"Error: {e}")

