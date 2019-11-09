"""
Calculates the factor amount for the invoice (a/c rec)
"""


def calc_factor_amt(invoice_value, LTV):
  factor_amnt = invoice_value*(LTV/100)
  str_amnt = str(round(factor_amnt))
  number_of_digits = len(str_amnt)
  number_to_divide_multiply = 10**number_of_digits
  round_number = round(factor_amnt/number_to_divide_multiply,2)
  return int(round_number*number_to_divide_multiply)