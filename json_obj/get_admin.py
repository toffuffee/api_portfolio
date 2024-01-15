from db_info.connect import get_admin_info_from_db
class GetAdmin:
    def get(self, environ):
        return get_admin_info_from_db()