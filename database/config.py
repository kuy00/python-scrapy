from orator import DatabaseManager

databases = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'ranking',
        'user': 'root',
        'password': 'gimuyeong1@',
        'prefix': ''
    }
}

db = DatabaseManager(databases)
