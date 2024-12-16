from flask import Flask, jsonify, request
from database import db
from os import environ
from models.meal import Meal
from dotenv import load_dotenv
from utils import is_valid_datetime


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("MY_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"mysql+pymysql://root:{environ.get("DB_PASSWORD")}@127.0.0.1:3306/daily-diet"

db.init_app(app)


@app.route("/meal", methods=["POST"])
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date = data.get("date")
    off_diet = data.get("off_diet")

    if name and description and date and off_diet:

        if not is_valid_datetime(date):
            return jsonify({"message": "Formato de data invalido"}), 400

        meal = Meal(
            name=name,
            description=description,
            date=date,
            off_diet=off_diet
        )

        db.session.add(meal)
        db.session.commit()

        return jsonify({"id": meal.id, "message": "Refeicao criada com sucesso"})

    else:
        return jsonify({"message": "Dados invalidos"}), 400


@app.route("/meal/<int:meal_id>", methods=["GET"])
def read_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({"message": "Refeicao nao encontrada"}), 404

    return jsonify({
        "id": meal.id,
        "name": meal.name,
        "description": meal.description,
        "date": meal.date,
        "off_diet": meal.off_diet
    })


@app.route("/meal/<int:meal_id>", methods=["PATCH"])
def update_meal(meal_id):
    data = request.json
    meal = Meal.query.get(meal_id)

    if not data:
        return jsonify({"message": "Payload vazio"}), 400

    if not meal:
        return jsonify({
            "message": "Refeicao nao encontrada"
        }), 404

    if data.get("name"):
        meal.name = data.get("name")

    if data.get("description"):
        meal.description = data.get("description")

    if data.get("date") and is_valid_datetime(data.get("date")):
        meal.date = data.get("date")

    if data.get("off_diet") is not None:
        meal.off_diet = data.get("off_diet")

    db.session.commit()

    return jsonify({
        "meal_id": meal.id,
        "message": f"Refeicao {meal.id} atualizada com sucesso"
    })


@app.route("/meal/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({"message": "Refeicao nao encontrada"}), 404

    db.session.delete(meal)
    db.session.commit()

    return jsonify({"message": "Refeicao deletada com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
