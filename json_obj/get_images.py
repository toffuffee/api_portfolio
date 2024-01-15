from db_info.connect import get_images_from_db
class GetImages:
    def get(self, environ):
        return get_images_from_db()