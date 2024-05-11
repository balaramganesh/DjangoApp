# routers.py

class SQLiteRouter:
    """
    A router to control all database operations on models routed to the
    'sqlite3_db' database.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read models routed to 'sqlite3_db' database go to SQLite3.
        """
        if model._meta.app_label == 'polls':  # Replace 'YourModelName' with the name of your model
            return 'sqlite3'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models routed to 'sqlite3_db' database go to SQLite3.
        """
        if model._meta.app_label == 'polls':
            return 'sqlite3'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if the models involved are routed to 'sqlite3_db'.
        """
        if obj1._meta.app_label == 'polls' or obj2._meta.app_label == 'polls':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'YourModelName' model only appears in the 'sqlite3_db'
        database.
        """
        if app_label == 'polls':
            # print('sql here:',model_name)
            return db == 'sqlite3'
        return None


class MySQLRouter:
    """
    A router to control all database operations on models routed to the
    'mysql_db' database.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read models routed to 'mysql_db' database go to MySQL.
        """
        if model._meta.app_label == 'orders':
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models routed to 'mysql_db' database go to MySQL.
        """
        if model._meta.app_label == 'orders':
            return 'mysql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if the models involved are routed to 'mysql_db'.
        """
        if obj1._meta.app_label == 'orders' or obj2._meta.app_label == 'orders':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'YourModelName' model only appears in the 'mysql_db'
        database.
        """
        if app_label == 'orders':
            # print('here:',model_name)
            return db == 'mysql'
        return None
