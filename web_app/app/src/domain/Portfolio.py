class Portfolio():
    def __init__(self,stock_id: int, name : str, acct_num : int, stock_tik : str , stock_qty : int, stock_pur_price : float, fund_name : str, fund_units : float, unit_pur_price : float, fund_nav : float, cash_bal : float):
        self.stock_id = stock_id
        self.name = name
        self.acct_num = acct_num
        self.stock_tik = stock_tik
        self.stock_qty = stock_qty
        self.stock_pur_price = stock_pur_price
        self.fund_name = fund_name
        self.fund_units = fund_units
        self.unit_pur_price = unit_pur_price
        self.fund_nav = fund_nav
        self.cash_bal = cash_bal
    pass