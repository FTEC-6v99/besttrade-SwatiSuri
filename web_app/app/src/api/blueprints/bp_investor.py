from flask import Blueprint,request
import json
import app.src.db.dao as dao
from app.src.domain.Investor import Investor
import typing as t

bp_investor = Blueprint('investor', __name__, url_prefix='/investor')



@bp_investor.route('/get-investor-by-id/<int:id>')
def get_investor_by_id(id: int) -> Investor:
    try:
        investor: Investor = dao.get_investor_by_id(id)
        if investor is None:
           return 200, []
        else:   
           return 200, json.dumps(investor.__dict__)
    except Exception as e:
        return 500, 'Oops, it is an error: '  + str(e)      


@bp_investor.route('/get-investor-by-name/<name>')
def get_investor_by_name(name: str) -> t.List[Investor]:
    investor = dao.get_investors_by_name(name)
    if investor is None:
        return 200, []
    else:
        return json.dumps(investor.__dict__)


@ bp_investor.route('/create-new-investor/<name>/<status>', methods=['POST'])
def create_investor(name, status, tier) -> Investor:
    investor = Investor(name, status, tier)
    dao.create_investor(investor)
    return '', 200


@bp_investor.route('/update-investor-name/<id>/<name>', methods=['PUT'])
def update_investor_name(id, name, tier):
    dao.update_investor_name(id, name, tier)
    return '', 200


@bp_investor.route('/delete-investor/<id>', methods=['DELETE'])
def delete_investor(id):
    dao.delete_investor(id)
    return '', 200