from flask import Blueprint,request
import json
import app.src.db.dao as dao
from app.src.domain.Account import Account
import typing as t

bp_account=  Blueprint('Account', __name__, url_prefix='/A--upgradeccount')


@bp_account.route('/get-account-by-id/<int:id>')
def get_account_by_id(id: int) -> Account:
    account = dao.get_account_by_id(id)
    try: 
        if account is None:
            return 200, []
        else:    
            return json.dumps(account.__dict__)
    except Exception as e:
        return 500, 'Oops, it is an error: '  + str(e)         


@bp_account.route('/get-accounts-by-investor-id/<int:investor_id>')
def get_accounts_by_investor_id(id: int) -> t.list[Account]:
    account = dao.get_account_by_id(id)
    if account is None:
            return 200, []
    else:    
            return json.dumps(account.__dict__)


@ bp_account.route('/create-account/<account_number>/<investor_id>/<balance>', methods=['POST'])
def create_account(acct_num, investor_id, acct_bal, acct_type) -> Account:
    account = Account(acct_num, investor_id, acct_bal, acct_type)
    dao.create_account(acct_num, investor_id, acct_bal, acct_type)
    return '', 200


@ bp_account.route('/update_acct_balance/<investor_id>/<account_balance>', methods=['PUT'])
def update_acct_balance(investor_id, acct_bal):
    dao.update_acct_balance(investor_id, acct_bal)
    return '', 200


@ bp_account.route('/delete-account/<investor_id>', methods=['DELETE'])
def delete_account(investor_id):
    dao.delete_account(investor_id)
    return '', 200