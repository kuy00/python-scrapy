from orator import Model
from database.config import db

Model = Model.set_connection_resolver(db)
