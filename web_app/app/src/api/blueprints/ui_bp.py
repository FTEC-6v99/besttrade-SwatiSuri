from flask import Blueprint, render_template
from app.src.domain.Investor import Investor
ui_bp = Blueprint('ui',__name__, url_prefix='/ui')

@ui_bp.route('/', methods = ['GET'])
def main():
    return render_template('Home.html')

@ui_bp.route('/about', methods = ['GET'])
def about():
    return render_template('About.html')

@ui_bp.route('/Investors', methods = ['GET'])
def investor():
    investors = []
    investors.append(Investor('Sneha Kumar','Active', 'Gold',1))
    investors.append(Investor('Li Jung','Inactive', 'Silver',2))
    investors.append(Investor('Chris Landon','Inactive', 'Platinum',3))
    investors.append(Investor('Rafiq Khan','Active', 'Bronze',4))
    return render_template('Investors.html', investors=investors)

@ui_bp.route('/Accounts', methods = ['GET'])
def account():
    return render_template('Accounts.html')

