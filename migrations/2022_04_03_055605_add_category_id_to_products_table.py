from orator.migrations import Migration


class AddCategoryIdToProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('products') as table:
            table.integer('category_id').unsigned()
            table.foreign('category_id').references('id').on('category')

    def down(self):
        with self.schema.table('products') as table:
            table.drop_foreign('products_category_id_foreign')
            table.drop_column('category_id')
