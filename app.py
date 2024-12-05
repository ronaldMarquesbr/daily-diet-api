from flask import Flask, jsonify
from database import db
from os import environ
from models.meal import Meal
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("MY_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"mysql+pymysql://root:{environ.get("DB_PASSWORD")}@127.0.0.1:3306/daily-diet"

db.init_app(app)


@app.route("/hello-world", methods=["GET"])
def teste():
    return jsonify({"message": "Teste"})


if __name__ == '__main__':
    app.run(debug=True)
