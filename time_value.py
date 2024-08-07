# future values
from math import e, log
# FOR ALL FUNCTIONS AS FOR USER INPUT OR MAYBE ASK BEFOREHAND!! RUN APPROPRIATE FUNCTION BASED ON INPUT
    # CLASS OR JUST USING ARGUEMENTS? MHMM WHAT TO DO. WILL NEED TO CHANGE THE FUNCTIONS BELOW AS WELL!!!

def get_user_inputs():
    lump_or_series = input("Please enter Lump sum or Series:")
    equal_or_unequal = input("Are your cash flows Equal or Unequal:")
    # if statements based on above
    if lump_or_series == 'Lump sum' and equal_or_unequal == 'Equal':
        cash_flows = input("Please enter the your cash flows in order:")
        interest_rates = input("Please enter the interest rates corresponding to your cash flows:")


def fv_lump_sum(present_value: int, interest_rate: float, num_periods: int, start_period: int=0, compounding_periods: int = 1):
    """
    This function calculates the future value of a lump sum. It can accommodate custom start periods and compounding periods.
    This function is not to be used for continous compounding.
    """

    # Check that arguments are valid
    if present_value < 0:
        return "Check your present value! It must be greater than 0!"
    if interest_rate < 0:
        return "Check your interest rate! It must be greater than 0!"
    if num_periods < 0:
        return "Check your number of periods! It must be greater than 0!"
    if start_period < 0:
        return "Check your start period! It must be greater than or equal to 0!"
    if compounding_periods < 1:
        return "Check your compounding periods! It must be greater than or equal to 1!"


    # calculate FV when start period is now
    if start_period == 0:

        rate_per_period = interest_rate / compounding_periods
        total_periods = num_periods * compounding_periods
        future_value = present_value(1 + rate_per_period)**num_periods
        
        return f"The Future value of your investment today is estimated to be: {future_value}"
    # calculate FV when start period is not now eg start_period != 0
    else: 

        rate_per_period = interest_rate / compounding_periods
        total_periods = num_periods * compounding_periods
        relevant_periods = total_periods - (start_period * compounding_periods)
        future_value = present_value(1 + interest_rate)**relevant_periods

        return f"The Future value of your investment today is estimated to be: {future_value}"
    

def fv_cont_compounding(present_value: int, interest_rate: float, num_periods: int, compounding_periods: int):
    """
    This function calculates the future value using continous compounding. Do not use this if you need other compounding periods.
    """

    # Error handling for parameters
    if present_value < 0:
        return "Check your present value! It must be greater than 0!"
    if interest_rate < 0:
        return "Check your interest rate! It must be greater than 0!"
    if num_periods < 0:
        return "Check your number of periods! It must be greater than 0!"
    if compounding_periods < 1:
        return "Check your compounding periods! It must be greater than or equal to 1!"

    period_rate = interest_rate / compounding_periods
    total_periods = num_periods * compounding_periods
    future_value = present_value * e**(period_rate * total_periods)

    return f"The Future value of your investment today is estimated to be: {future_value}"

def calc_effective_rates(interest_rate: float, compounding_periods: int = 1):
    """
    Calculates the effective interest rate (EAR). The compounding periods is for one year only!
    
    """
    # Error handling for parameters
    if interest_rate < 0:
        return "Your interest rate must be greater than 0!"
    if compounding_periods < 1 or compounding_periods > 365:
        return "Compounding periods must be between 1 and 365, inclusive. Common compounding periods are annual (1), bi-annual (2), quarterly (4), monthly (12), and daily (365)"

    # check if compounding periods is more than annual
    if compounding_periods != 1:
        ear = (1 + interest_rate)**compounding_periods
        return f"Here is your EAR: {ear}"
    else:
        ear = e**interest_rate - 1
        return f"Here is your EAR: {ear}"
    
def calc_stated_rate(effective_rate: float, compounding_periods: int = 1):
    """
    This function calculates the stated interest rate, which is what lenders typically quote"
    """

    # Error handling for parameters
    if effective_rate < 0:
        return "Your effective rate must be greater than 0"
    if compounding_periods < 1:
        return "Your compounding periods must be greater than or equal to 1"

    # Check if not annual compounding
    if compounding_periods != 1:
        stated_interest = (1 + effective_rate)**1/compounding_periods - 1
        return f"Here is the stated interest rate: {stated_interest}"
    else:
        stated_interest = log(1 + effective_rate)
        f"Here is the stated interest rate: {stated_interest}"

def fv_equal_cash_flows(annuity: int, interest_rate: float, num_periods: int, compounding_periods: int = 1):
    """
    Calculates the FV of annuities where the cash flows are equal. 
    """

    if annuity < 0:
        return "Your annuity must be greater than 0."
    if interest_rate < 0:
        return "Your interest rate must be positive."
    if num_periods < 0:
        return "Your number of periods must be greater than 0"
    if compounding_periods < 1:
        return "Your compounding periods must be greater than 1"

    # check if annual compounding or not
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
    
def fv_unequal_cash_flows(cash_flows: int, interest_rate: float, num_periods: int, compounding_periods: int = 1):
    """
    Calculates the FV of unequal cash flows. Cash flows should be entered in order within a list.
    Interest rates should also be entered in order matching the cash flows. 
    """
    # maybe use a dictionary here? need to get the inputs as well I guess