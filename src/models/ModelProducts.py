import math
import os
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_FOLDER = 'src/static/media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def delete_image_from_server(image_path):
    full_path = os.path.abspath(image_path)
    full_path = os.path.join(os.getcwd(), "src", "static", "media", os.path.basename(full_path))
    if os.path.exists(full_path):
        os.remove(full_path)
    else:
        print(f"File not found: {full_path}")
 
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
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
        available_value = 1 if available.lower() == 'true' else 0

        if image_upload and allowed_file(image_upload.filename, ALLOWED_EXTENSIONS):
            filename, ext = os.path.splitext(secure_filename(image_upload.filename))
            filename_with_date = f"{filename}-{formatted_date}{ext}"
            ext = "/static/media/"
            image_upload.save(os.path.join(UPLOAD_FOLDER, filename_with_date))
            filename_with_ext = ext + filename_with_date
            cur = db.connection.cursor()
            cur.execute("INSERT INTO foodMenu (nameFood, priceFood, imageUrl, descriptionFood, available, idCategory) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (name_food, price_food, filename_with_ext, description_food, available_value, id_category))
            db.connection.commit()
            cur.close()

            image_path = f'/static/media/{filename_with_date}'
            return image_path
        else:
            return "Invalid file type"
        
    def get_product_by_id(self, db, product_id):
        cur = db.connection.cursor()
        cur.execute("SELECT idFood, nameFood, priceFood, imageUrl, descriptionFood, available, idCategory FROM foodMenu WHERE idFood = %s", (product_id,))
        product = cur.fetchone()
        cur.close()
        return product
     
    def update_product(self, db, product_id, name_product, price_food, description_food, available_food, idCategory_food):
        cur = db.connection.cursor()
        cur.execute("UPDATE foodMenu SET nameFood = %s, priceFood = %s, descriptionFood = %s, available = %s, idCategory = %s WHERE idFood = %s",
                    (name_product, price_food, description_food, available_food, idCategory_food, product_id))
        db.connection.commit()
        cur.close()

        
    def delete_product(self, db, product_id, image_path):
        cur = db.connection.cursor()
        cur.execute("DELETE FROM foodMenu WHERE idFood = %s", (product_id,))
        db.connection.commit()
        cur.close()
        try:
            delete_image_from_server(image_path)
            print(f"Product image deleted successfully at path {image_path}.")
        except FileNotFoundError:
            print(f"File not found at path {image_path}.")

