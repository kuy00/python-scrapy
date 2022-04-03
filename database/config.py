from orator import DatabaseManager

databases = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'ranking',
        'user': 'test',
        'password': 'test1!',
        'prefix': ''
    }
}

db = DatabaseManager(databases)
