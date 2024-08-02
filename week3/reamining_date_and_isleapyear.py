"""
Create a Python program that uses the dateMme module to accomplish the
following tasks:
    a. Calculate the number of days remaining until a specific future date, such as a
        birthday or holiday.
    b. Implement a function using the dateMme module to determine if a given year
        is a leap year or not.
"""
# import datetime class from datetime module
from datetime import datetime

# Creating given funtions
def days_until_future_date(date):
    """
    Funtion to calculate the number of days remaining from future date
    para:
        date - String - future date
    return type: int - days remaining
    """
    future_date = datetime.strptime(date,'%Y-%m-%d').date()
    today = datetime.today().date()
    delta = future_date - today
    return delta.days


def is_leap_year(year):
    """
    Funtion to find wheather the year is leap year or not
    para:
        year - int
    return type:  bool
    """
    if((year%4 == 0 and year%100!=0) or (year%400 == 0)):
        return True
    else:
        return False


#main
def main():
    future_date = input("Enter the date: (YYYY-MM-DD) : ")
    rem_days = days_until_future_date(future_date)
    print(f"No. of days remaining: { future_date } : { rem_days } days.")


    year = int(input("Enter the year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# if this is not a module
if __name__ == '__main__':
    main()
