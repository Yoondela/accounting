from user import authentication
from transections import journal
from banking import reconciliation
# from fvb import reconciliation


authentication.authenticate_user()
journal.receive_income(100.00)
journal.pay_expense(100.00)
reconciliation.do_reconciliation()
