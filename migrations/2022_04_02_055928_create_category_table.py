from orator.migrations import Migration


class CreateCategoryTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('category') as table:
            table.increments('id')
            table.string('name')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('category')
