from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)


db_user = 'root'
db_pass = 'vacationplanner'
db_name = db_user
db_host = 'database_backend'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)
res = db.execute("SELECT version()")
for (i) in res:
    print(i[0])

class Product(Resource):
    def __init__(self) -> None:
        super().__init__()
        conn = psycopg2.connect("")

    def get(self):
        return {
            's'
        }

api.add_resource(Product, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

print("1")
print("2")

