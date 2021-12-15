from flask import Flask
from app.src.api.blueprints.bp_investor import bp_investor
from app.src.api.blueprints.bp_account import bp_account
from app.src.api.blueprints.bp_portfolio import bp_portfolio
from app.src.api.blueprints.ui_bp import ui_bp
app = Flask(__name__)
app.register_blueprint(bp_investor)
app.register_blueprint(bp_account)
app.register_blueprint(bp_portfolio)
app.register_blueprint(ui_bp)


if __name__ == '__main__':
    app.run(port=8080)
    
       