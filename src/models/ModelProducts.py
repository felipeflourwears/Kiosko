import math
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'src/static/media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

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
    
    def add_product(self, db, name_food, price_food, image_upload, description_food, available, id_category):
        available_value = 1 if available.lower() == 'true' else 0

        if image_upload and allowed_file(image_upload.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(image_upload.filename)
            ext = "/static/media/"
            image_upload.save(os.path.join(UPLOAD_FOLDER, filename))
            filename_with_ext=ext+filename
            cur = db.connection.cursor()
            cur.execute("INSERT INTO foodMenu (nameFood, priceFood, imageUrl, descriptionFood, available, idCategory) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (name_food, price_food, filename_with_ext, description_food, available_value, id_category))
            db.connection.commit()
            cur.close()

            image_path = f'/static/media/{filename}'
            return image_path
        else:
            return "Invalid file type"

