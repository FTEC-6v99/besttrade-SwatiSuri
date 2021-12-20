from flask import Blueprint, render_template
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio
ui_bp = Blueprint('ui',__name__, url_prefix='/ui')

@ui_bp.route('/', methods = ['GET'])
def main():
    return render_template('Home.html')

@ui_bp.route('/about', methods = ['GET'])
def about():
    return render_template('About.html')

@ui_bp.route('/investors', methods = ['GET'])
def investor():
    investors = []
    investors.append(Investor('Sneha Kumar','Active', 'Gold',1))
    investors.append(Investor('Li Jung','Inactive', 'Silver',2))
    investors.append(Investor('Chris Landon','Inactive', 'Platinum',3))
    investors.append(Investor('Rafiq Khan','Active', 'Bronze',4))
    return render_template('Investors.html', investors=investors)

@ui_bp.route('/accounts', methods = ['GET'])
def account():
    accounts = []
    accounts.append(Account('Sneha Kumar',1,123456, 20000,'Investor'))
    accounts.append(Account('Li Jung',2,127890,25000, 'Trader'))
    accounts.append(Account('Chris Landon',3,126543,30000, 'Trader'))
    accounts.append(Account('Rafiq Khan',4,120987,35000, 'Investor'))
    return render_template('Accounts.html', accounts=accounts)

@ui_bp.route('/portfolios', methods = ['GET'])
def portfolio():
    portfolios = []
    portfolios.append(Portfolio(10, 'Sneha Kumar', 123456, 'AAPL', 10, 25.00, 'Growth Fund', 166, 30.00, 35.00, 30000))
    portfolios.append(Portfolio(11, 'Li Jung', 1237890, 'GOOGL', 15, 30.00, 'ESS Fund', 225, 450.00, 700.00, 55000))
    portfolios.append(Portfolio(12, 'Chris Landon', 126543, 'NFLX', 20, 45.00, 'Gold Fund', 110, 1500.00, 1900.00, 100000))
    portfolios.append(Portfolio(13, 'Rafiq Khan', 120987, 'AMZN', 15, 55.00, 'Index Fund', 55, 600.00, 1050.00, 25000))
    return render_template('Portfolios.html', portfolios=portfolios)

