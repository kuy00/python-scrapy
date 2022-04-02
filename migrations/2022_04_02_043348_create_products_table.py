from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        with self.schema.create('products') as table:
            table.increments('id')
            table.string('brand', 100)
            table.string('name', 100)

    def down(self):
        self.schema.drop('products')
