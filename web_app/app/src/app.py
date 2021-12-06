from flask import Flask
from app.src.blueprints.bp_investor import bp_investor
from app.src.blueprints.bp_account import bp_account
from app.src.blueprints.bp_portfolio import bp_portfolio


app = Flask(__name__)
app.register_blueprint(bp_investor)
app.register_blueprint(bp_account)
app.register_blueprint(bp_portfolio)


if __name__ == '__main__':
    app.run(port=8080)
    
