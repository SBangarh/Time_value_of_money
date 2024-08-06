# future values
from math import e, log


def fv_lump_sum(present_value: int, interest_rate: float, num_periods: int, start_period: int=0, compounding_periods: int):
    """
    This function calculates the future value of a lump sum. It can accommodate custom start periods and compounding periods.
    This function is not to be used for continous compounding.
    """
    # calculate FV when start period is now
    if start_period == 0:

        rate_per_period = interest_rate / compounding_periods
        total_periods = num_periods * compounding_periods
        future_value = present_value(1 + rate_per_period)**num_periods
        
        return f"The Future value of your investment today is estimated to be: {future_value}"
    
    else: 

        rate_per_period = interest_rate / compounding_periods
        total_periods = num_periods * compounding_periods
        relevant_periods = total_periods - (start_period * compounding_periods)
        future_value = present_value(1 + interest_rate)**relevant_periods

        return f"The Future value of your investment today is estimated to be: {future_value}"
    

def fv_cont_compounding(present_value: int, interest_rate: float, num_periods: int, compounding_periods: int):
    """
    Function doc
    """
    period_rate = interest_rate / compounding_periods
    total_periods = num_periods * compounding_periods
    future_value = present_value * e**(period_rate * total_periods)

    return f"The Future value of your investment today is estimated to be: {future_value}"

def calc_effective_rates(interest_rate: float, compounding_periods: int = 1):
    """
    function docs go here
    compounding periods for one year only
    """

    if compounding_periods != 1:
        ear = (1 + interest_rate)**compounding_periods
        return f"Here is your EAR: {ear}"
    else:
        ear = e**interest_rate - 1
        return f"Here is your EAR: {ear}"
    
def calc_stated_rate(effective_rate: float, compounding_periods: int = 1):
    """
    doc strings
    """

    if compounding_periods != 1:
        stated_interest = (1 + effective_rate)**1/compounding_periods - 1
        return f"Here is the stated interest rate: {stated_interest}"
    else:
        stated_interest = log(1 + effective_rate)
        f"Here is the stated interest rate: {stated_interest}"

def fv_equal_cash_flows(annuity: int, interest_rate: float, num_periods: int, compounding_periods: int = 1):
    """
    docs
    """

    if compounding_periods != 1:
        rate_per_period = interest_rate / compounding_periods
        total_periods = num_periods * compounding_periods
        annuity_factor = (((1 + rate_per_period)**total_periods - 1) / rate_per_period)
        future_value = annuity*annuity_factor

        return f"Here is the Future Value of your annuity: {future_value}"
    else:
        annuity_factor = (((1 + interest_rate)**num_periods - 1) / interest_rate)
        future_value = annuity*annuity_factor

        return f"Here is the Future Value of your annuity: {future_value}"
    
def fv_unequal_cash_flows((annuity: int, interest_rate: float, num_periods: int, compounding_periods: int = 1))