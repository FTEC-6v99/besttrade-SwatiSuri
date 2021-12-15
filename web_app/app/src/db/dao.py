# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete
import typing as t
from typing_extensions import ParamSpecArgs
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection
import config
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio 

def get_cnx() -> MySQLConnection:
    return connect(**config.dbparams)

'''
    Investor DAO functions
'''

def get_all_investor() -> t.list[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors

def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where id = %s'
    cursor.execute(sql, (id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        investor = Investor(row['name'], row['status'], row['id'])
        return investor 

def get_investors_by_name(name: str) -> t.list[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where name = %s'
    cursor.execute(sql, (name,))
    if cursor.rowcount == 0:
        investors = []
    else:
        rows = cursor.fetchall()
        for row in rows:
            investors.append(Investor('Sneha Kumar','Active', 'Gold',1))
            investors.append(Investor('Li Jung','Inactive', 'Silver',2))
            investors.append(Investor('Chris Landon','Inactive', 'Platinum',3))
            investors.append(Investor('Rafiq Khan','Active', 'Bronze',4))
    db_cnx.close()
    return investors


def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()

def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s'
    cursor.execute(sql, (id,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set name = %s where id = %s'
    cursor.execute(sql, (id, name))
    db_cnx.commit()
    db_cnx.close()

def update_investor_status(id: int, status: str) -> None:
    '''
        Update the inestor status [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set status = %s where id = %s'
    cursor.execute(sql, (id, status))
    db_cnx.commit()
    db_cnx.close()

'''
    Account DAO functions
'''
def get_all_accounts() -> t.list[Account]:
    accounts: list[Account] = []
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor(dictionary=True) 
    select: str = 'select * from Account'
    curs.execute(select)
    rows: list[dict] = curs.fetchall()
    if len(rows) == 0:
        bt_cnx.close()  
        return []
    accounts = []
    for row in rows:
        accounts.append(Account(row['acct_num'], row['investor_id'], row['acct_bal'], row['acct_type']))
    bt_cnx.close()
    return accounts
pass

def get_account_by_id(id: int) -> Account:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor(dictionary=True)
    select: str = 'select * from accounts where id = %s'
    curs.execute(select, (id,))
    row = curs.fetchone()
    if len(row) == 0:
        bt_cnx.close()  
        return []
    account = []
    account = Account(row['acct_num'], row['investor_id'], row['acct_bal'], row['acct_type'])
    return account
pass

def get_accounts_by_investor_id(investor_id: int) -> t.list[Account]:
    accounts: list[Investor] = []
    bt_cnx = get_cnx()
    curs = bt_cnx.curs(dictionary=True)
    select: str = 'select * from accounts where investor_id = %s'
    curs.execute(select, (investor_id,))
    rows = curs.fetchall()
    if len(rows) == 0:
        bt_cnx.close()  
        return []
    accounts = []  
    for row in rows:
            accounts.append(row['acct_num'], row['investor_id'], row['acct_bal'], row['acct_type'])
    bt_cnx.close()
    return accounts
pass

def delete_account(investor_id: int) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    delete = 'delete from account where investor_id = %s'
    curs.execute(delete, (investor_id,))
    bt_cnx.commit()
    bt_cnx.close()
pass

def update_acct_balance(investor_id: int, acct_bal: float) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    update = 'update acct_blance set acct_bal = %s where id = %s'
    curs.execute(update, (investor_id, acct_bal))
    bt_cnx.commit()
    bt_cnx.close()
pass

def create_account(account: Account) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    insert = 'insert into account (acct_num, investor_id, acct_bal, acct_type) values (%s, %s, %s, %s)'
    curs.execute(insert, (account.acct_num, account.investor_id, account.acct_bal, account.acct_type))
    bt_cnx.commit()
    bt_cnx.close()
pass

'''
    Portfolio DAO functions
'''
def get_all_portfolios() -> t.list[Portfolio]:
    portfolios: list[Portfolio] = []
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor(dictionary=True) 
    select: str = 'select * from Portfolio'
    curs.execute(select)
    rows: list[dict] = curs.fetchall()
    if len(rows) == 0:
        bt_cnx.close()  
        return []
    portfolios = []
    for row in rows:
        portfolios.append(Portfolio(row['stock_id'], row['acct_num'], row['stock_tik'], row['stock_qty'], row['stock_pur_price'], row['fund_name'], row['fund_units'], row['unit_pur_price'], row['nav'], row['cash']))
    bt_cnx.close()
    return portfolios
pass

def get_porfolios_by_acct_id(acct_num: int) -> t.list[Portfolio]:
    portfolios: list[Portfolio] = []
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor(dictionary=True)
    select: str = 'select * from portfolio where acct_num = %s'
    curs.execute(select, (acct_num,))
    rows = curs.fetchone()
    if len(rows) == 0:
        bt_cnx.close()  
        return []
    portfolios = []
    for row in rows:
         portfolios = Account(row['acct_num'], row['investor_id'], row['acct_bal'], row['acct_type'])
    return portfolios
pass

def get_portfolio_by_id(stock_id: int) -> t.list[Portfolio]:
    portfolios: list[Investor] = []
    bt_cnx = get_cnx()
    curs = bt_cnx.curs(dictionary=True)
    select: str = 'select * from portfolios where investor_id = %s'
    curs.execute(select, (stock_id,))
    rows = curs.fetchall()
    if len(rows) == 0:
        bt_cnx.close()  
        return []
    portfolios = []  
    for row in rows:
            portfolios.append(Portfolio(row['stock_id'], row['acct_num'], row['stock_tik'], row['stock_qty'], row['stock_pur_price'], row['fund_name'], row['fund_units'], row['unit_pur_price'], row['nav'], row['cash']))
    bt_cnx.close()
    return portfolios
pass

def update_portfolio_name(stock_id: int, name: str) -> None:
    db_cnx = get_cnx()
    curs = db_cnx.cursor()
    update = 'update portfolio set name = s%'
    curs.execute(update, (stock_id, name))
    db_cnx.commit()
    db_cnx.close()
pass
      
def create_portfolio(portfolio: Portfolio) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    insert = 'insert into portfolio (stock_id, name, acct_num, stock_tik, stock_qty, stock_pur_price, float, fund_name, fund_units, unit_pur_price, fund_nav, cash_bal) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    curs.execute(insert, (portfolio.stock_id, portfolio.name, portfolio.acct_num, portfolio.stock_tik, portfolio.stock_qty, portfolio.stock_pur_price, portfolio.fund_name, portfolio.fund_units, portfolio.unit_pur_price, portfolio.fund_nav, portfolio.cash_bal))
    bt_cnx.commit()
    bt_cnx.close()
pass

def delete_portfolio(stock_id: int) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    delete = 'delete from portfolio where stock_id = %s'
    curs.execute(delete, (stock_id,))
    bt_cnx.commit()
    bt_cnx.close()
    return delete_portfolio
pass


def buy_stock(stock_tik: str, stock_pur_price: float, stock_qty: int, acct_num : int) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    insert = 'insert into portfolio (stock_tik, stock_pur_price, stock_qty, acct_num) values (%s, %s, %s,%s)'
    curs.execute(insert, (stock_tik, stock_pur_price, stock_qty, acct_num))
    bt_cnx.commit()
    bt_cnx.close() #missing values account num
    pass

def sell_stock(stock_tik: str, stock_qty: int, sale_price: float) -> None:
   def update_stock_qty(stock_tik: str, stock_qty: int) -> None:
      bt_cnx = get_cnx()
      curs = bt_cnx.cursor()
      update = 'update portfolio set stock_qty = 10 where stock_tik = AAPL'
      curs.execute(update, (stock_tik, stock_qty))
      bt_cnx.commit()
      bt_cnx.close()
      print (update_stock_qty)
   def update_acct_balance(investor_id: int, acct_bal: float) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    update = 'update acct_blance set acct_bal = 100 where id = 1'
    curs.execute(update, (investor_id, acct_bal))
    bt_cnx.commit()
    bt_cnx.close()
    print (update_acct_balance)
   def update_stock_qty(stock_tik: str, stock_qty: int) -> None:
      bt_cnx = get_cnx()
      curs = bt_cnx.cursor()
      update = 'update portfolio set stock_qty = 8 where stock_tik = AAPL'
      curs.execute(update, (stock_tik, stock_qty))
      bt_cnx.commit()
      bt_cnx.close()
      print (update_stock_qty)
   def update_acct_balance(investor_id: int, acct_bal: float) -> None:
    bt_cnx = get_cnx()
    curs = bt_cnx.cursor()
    update = 'update acct_blance set acct_bal = 104 where id = 1'
    curs.execute(update, (investor_id, acct_bal))
    bt_cnx.commit()
    bt_cnx.close()
    print (update_acct_balance)  
pass