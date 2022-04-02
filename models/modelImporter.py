import importlib


class ModelImporter:
    @staticmethod
    def get_model(model):
        module = importlib.import_module('models.{}'.format(model.lower()))
        return getattr(module, model)
