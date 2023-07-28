#import pdb; pdb.set_trace()


class money_moves:

    def __init__(self, **kargs):
        self.money_amount = kargs["money_amount"]
        self.invest_rate = kargs["invest_rate"] / 100
        self.monthly_money_available = kargs["monthly_money_available"]
        self.loan_amount = kargs["loan_amount"]
        self.loan_rate = kargs["loan_rate"] / 100
        self.loan_months = kargs["loan_years"] * 12
        self.monthly_mortgage_payment = self.calculate_monthly_mortgage_payment()


    """
    M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
        M = Total monthly payment
        P = The total amount of your loan
        I = Your interest rate, as a monthly percentage
        N = The total amount of months in your timeline for paying off your mortgage
    """
    def calculate_monthly_mortgage_payment(self):
        monthly_loan_rate = self.loan_rate / 12
        one_plus_i_pow_n = pow(1 + monthly_loan_rate, self.loan_months)
        self.monthly_mortgage_payment = self.loan_amount * (monthly_loan_rate * one_plus_i_pow_n) / (one_plus_i_pow_n - 1)


    def simulate_all_months(self):
        monthly_invest_rate = self.invest_rate / 12
        print(f'monthly interest on your money = {monthly_invest_rate}')
        curr_money_amount = self.money_amount
        for month in range(1, self.loan_months + 1):
            curr_money_amount += curr_money_amount * monthly_invest_rate
            # Right now, assume we want to add all monthly available money to savings
            # In the future, give option to contribute monthly available money to paying off loan
            curr_money_amount += self.monthly_money_available
            if ((month % 12) == 0):
                year = int(month / 12)
                print(f'current money after {year} years: {curr_money_amount:,.0f}')


def get_money_moves_vars():
    vars = dict()
    vars["money_amount"] = int(input("\nhow much money do you currently have?\n"))
    vars["invest_rate"] = float(input("\nwhat interest will you get on your money in percent?\n"))
<<<<<<< HEAD
    vars["loan_amount"] = int(input("\nwhat is the loan amount?\n"))
    vars["loan_rate"] = float(input("\nwhat is the loan interest rate in percent?\n"))
    vars["loan_years"] = int(input("\nhow many years is your loan?\n"))
    vars["salary"] = int(input("\nwhat is your salary?\n"))
=======
    vars["monthly_money_available"] = int(input("\nhow much money do you have available per month?\n"))
    vars["loan_amount"] = int(input("\nwhat is the loan amount?\n"))
    vars["loan_rate"] = float(input("\nwhat is the loan interest rate in percent?\n"))
    vars["loan_years"] = int(input("\nhow many years is your loan?\n"))
>>>>>>> b7893c0 (calculate how much investment becomes after x years)
    return vars

def test_money_moves_vars():
    vars = dict()
    vars["money_amount"] = 500000
    vars["invest_rate"] = 5.0
    vars["monthly_money_available"] = 0
    vars["loan_amount"] = 500000
    vars["loan_rate"] = 5.0
    vars["loan_years"] = 30
    vars["home_gain_rate"] = 5.0
<<<<<<< HEAD
    vars["salary"] = 120000
=======
>>>>>>> b7893c0 (calculate how much investment becomes after x years)
    return vars


if __name__ == "__main__":
<<<<<<< HEAD
    #vars = get_money_moves_vars()
    vars = test_money_moves_vars()
=======
    vars = get_money_moves_vars()
    #vars = test_money_moves_vars()
>>>>>>> b7893c0 (calculate how much investment becomes after x years)
    my_money = money_moves(**vars)
    my_money.simulate_all_months()
