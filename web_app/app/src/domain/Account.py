class Account():
    def __init__(self, name: str, acct_num: int, investor_id: int, acct_bal: float, acct_type: str):
        self.name = name
        self.acct_num = acct_num
        self.investor_id = investor_id
        self.acct_bal = acct_bal
        self.acct_type = acct_type