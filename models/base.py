from orator import Model
from database.config import db


class Base(Model):
    Model.set_connection_resolver(db)
