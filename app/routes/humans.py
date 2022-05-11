from crypt import methods
from flask import Blueprint, jsonify, request, abort, make_response
from app.models.humans import Human
from app.models.cats import Cat
from app import db


humans_bp = Blueprint("humans_bp", __name__, url_prefix="/humans")

def get_human_of_abort(human_id):
    try:
        human_id = int(human_id)
    except ValueError:
        rsp = {"msg":f"Invalid id {human_id}"}
        abort(make_response(jsonify(rsp), 400))

    human = Human.query.get(human_id)
    if human is None:
        rsp = {"msg":f"Could not find human with id {human_id}"}
        abort(make_response(jsonify(rsp), 404))
    return human

@humans_bp.route("", methods=["POST"])
def create_human():
    request_body = request.get_json()
    new_human = Human(name=request_body["name"])
    db.session.add(new_human)
    db.session.commit()

    return {
        "msg": f"Successfully created {new_human.name} with id {new_human.id}"
    }, 201

@humans_bp.route("", methods=["GET"])
def get_all_humans():
    humans = Human.query.all()

    rsp = []
    for human in humans:
        rsp.append(
            {
                "name": human.name
            }
        )
    return jsonify(rsp), 200

@humans_bp.route("/<human_id>/cats", mothod=["POST"])
def create_cat(human_id):
    human = get_human_of_abort(human_id)
    request_body = request.get_json()

    new_cat = Cat(
        name = request_body["name"],
        color = request_body["color"],
        age = request_body["age"],
        human = human
    )

    db.session.add(new_cat)
    db.session.commit()

    return {
        "msg": f"New cat {new_cat.name} created for {human.name}"
    }, 201

@humans_bp.route("/<human_id>/cats", mothod=["GET"])
def get_cats(human_id):
    human = get_human_of_abort(human_id)
    
    rsp = []
    for cat in human.cats:
        rsp.append(
            {
                "id": cat.id,
                "name": cat.name,
                "color": cat.color,
                "age": cat.age
            }
        )
    return jsonify(rsp), 200