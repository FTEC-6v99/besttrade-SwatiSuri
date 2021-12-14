from flask import Blueprint,request
import json
import app.src.db.dao as dao
from app.src.domain.Portfolio import Portfolio
import typing as t

bp_portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@bp_portfolio.route('/get-all-portfolio')
def get_all_portfolios() -> t.List[Portfolio]:
    portfolio = dao.get_all_portfolios()
    if portfolio is None:
            return 200, []
    else:    
            return json.dumps(portfolio.__dict__)

@bp_portfolio.route('/get-portfolio-by-id/<int:id>')
def get_portfolio_by_id(id: int) ->  Portfolio:
    portfolio = dao.get_portfolio_by_id(id)
    if portfolio is None:
            return 200, []
    else:    
            return json.dumps(portfolio.__dict__)


@bp_portfolio.route('/create-portfolio/<name>/<status>', methods=['POST'])
def create_portfolio(name, status) -> Portfolio:
    portfolio = Portfolio(name, status)
    dao.create_portfolio(portfolio)
    return '', 200


@bp_portfolio.route('/update-portfolio-name/<id>/<name>', methods=['PUT'])
def update_portfolio_name(id, name):
    dao.update_portfolio_name(id, name)
    return '', 200


@bp_portfolio('/delete-portfolio/<id>', methods=['DELETE'])
def delete_portfolio(id):
    dao.delete_portfolio(id)
    return '', 200