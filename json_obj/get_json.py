from db.connect import get_products_from_db
class GetProducts:
    def get(self, environ):
        return get_products_from_db()