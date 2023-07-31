#import pdb; pdb.set_trace()
import argparse


class money_moves:

    def __init__(self, **kargs):
        self.initial_money_available = kargs["initial_money_available"]
        self.invest_rate = kargs["invest_rate"] / 100.0
        self.monthly_money_available = kargs["salary_available"] / 12.0
        self.home_price = kargs["home_price"]
        self.down_payment_amount = self.home_price * (kargs["down_payment"] / 100.0)
        self.loan_amount = self.home_price - self.down_payment_amount
        print(f'loan amount = {self.loan_amount}')
        self.loan_rate = kargs["loan_rate"] / 100.0
        self.loan_months = kargs["loan_years"] * 12

        property_tax_monthly_rate = kargs["property_tax_rate"] / 100.0 / 12.0
        self.additional_monthly_payments = kargs["hoa_per_month"] + (kargs["home_insurance"] / 12.0) + kargs["utilities_per_month"] + (self.home_price * property_tax_monthly_rate)
        self.monthly_mortgage_payment = self.calculate_monthly_home_payment()
        if self.monthly_money_available < self.monthly_mortgage_payment:
            print(f'you can\'t affor the mortgage. mortgage = {self.monthly_mortgage_payment}, monthly savings = {self.monthly_money_available}')
            exit()
        print(f'monthly mortgage payment = {self.monthly_mortgage_payment}')


    """
    M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
        M = Total monthly payment
        P = The total amount of your loan
        I = Your interest rate, as a monthly percentage
        N = The total amount of months in your timeline for paying off your mortgage
    """
    def calculate_monthly_home_payment(self):
        monthly_loan_rate = self.loan_rate / 12.0
        one_plus_i_pow_n = pow(1 + monthly_loan_rate, self.loan_months)
        monthly_mortgage_payment = self.loan_amount * (monthly_loan_rate * one_plus_i_pow_n) / (one_plus_i_pow_n - 1)
        monthly_home_payment = monthly_mortgage_payment + self.additional_monthly_payments
        return monthly_home_payment


    def simulate_all_months(self):
        monthly_invest_rate = self.invest_rate / 12
        curr_money_available = self.initial_money_available - self.down_payment_amount
        for month in range(1, self.loan_months + 1):
            curr_money_available += curr_money_available * monthly_invest_rate
            # Right now, assume we want to add all monthly available money to savings
            # In the future, give option to contribute monthly available money to paying off loan
            curr_money_available += self.monthly_money_available
            curr_money_available -= self.monthly_mortgage_payment
            if ((month % 12) == 0):
                year = int(month / 12)
                print(f'current money after {year} years: {curr_money_available:,.0f}')


def get_money_moves_vars():
    vars = dict()
    vars["initial_money_available"] = int(input("\nhow much money do you currently have?\n"))
    vars["invest_rate"] = float(input("\nwhat interest will you get on your money in percent?\n"))
    vars["salary_available"] = int(input("\nhow much of your salary will you use for mortgage + savings?\n"))
    vars["loan_amount"] = int(input("\nwhat is the loan amount?\n"))
    vars["loan_rate"] = float(input("\nwhat is the loan interest rate in percent?\n"))
    vars["loan_years"] = int(input("\nhow many years is your loan?\n"))
    vars["home_gain_rate"] = float(input("\nwhat percent in price does the home increase per year?\n"))
    return vars

def test_money_moves_vars():
    vars = dict()
    vars["initial_money_available"] = 550000
    vars["invest_rate"] = 7.0
    vars["salary_available"] = 70000
    vars["loan_rate"] = 6.875
    vars["loan_years"] = 30
    vars["down_payment"] = 20
    vars["home_price"] = 625000
    vars["property_tax_rate"] = 1.21
    vars["home_gain_rate"] = 4.5
    vars["hoa_per_month"] = 92
    vars["home_insurance"] = 2000 # per year
    vars["utilities_per_month"] = 150
    return vars


def parse_args():
    parser = argparse.ArgumentParser(description='get mortgage vs. investment info')
    parser.add_argument('--test', action='store_true')
    return vars(parser.parse_args())


if __name__ == "__main__":
    args = parse_args()
    if args['test']:
        vars = test_money_moves_vars()
    else:
        vars = get_money_moves_vars()
    my_money = money_moves(**vars)
    my_money.simulate_all_months()
