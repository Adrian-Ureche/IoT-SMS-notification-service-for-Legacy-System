from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import Keys

class CloudView:
    def __init__(self):
        self.table_service = TableService(connection_string=Keys.connection_string)
        self.table_name = Keys.table_name

    def create_or_update_entity(self, widget_id, value):
        widget = Entity()
        widget.PartitionKey = 'Widget'
        widget.RowKey = widget_id
        widget.Value = value

        self.table_service.insert_or_replace_entity(self.table_name, widget)

        print(f"Entitatea a fost creată sau actualizată cu succes în tabelul {self.table_name}. {widget_id}")
