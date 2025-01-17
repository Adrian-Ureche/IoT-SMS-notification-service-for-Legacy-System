from flask import Flask, request, jsonify
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import Keys

app = Flask(__name__)

# Conectarea la Azure Table Storage
table_service = TableService(account_name=Keys.account_name, account_key=Keys.account_key)


# Route pentru GET
@app.route('/widgets', methods=['GET'])
def get_data():
    try:
        entities = table_service.query_entities(Keys.table_name)

        data_list = []
        for entity in entities:
            data_list.append({
                'PartitionKey': entity.PartitionKey,
                'RowKey': entity.RowKey,
                'Value': entity.Value
            })

        return jsonify(data_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)