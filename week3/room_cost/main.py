"""
Create a Python funcMon that performs the following tasks:
    a. Accepts three parameters: length, width, and height representing the
        dimensions of room.
    b. Computes the area to be whitewashed using the function
        whitewashing_Area().
    c. Calculates the cost of whitewashing at a rate of Rs.15/- per sq.m using the
        function whitewashing_Cost().
    d. Computes the cost of flooring at different rates: Rs.100/- per sq.m for mosaic
        flooring and
    e. Rs.55/- per sq.m for cement flooring using the function flooring_Cost().
    f. The function should display the calculated costs for whitewashing and
        flooring.
"""

#importing the module created
import room_cost as rc

def main():
    # Getting the details for user
    length = float(input("Enter the length (in feet): "))
    width = float(input("Enter the width (in feet): "))
    height = float(input("Enter the height (in feet): "))

    # Displaying the results
    rc.display_costs(length,width,height)

# if this is not a module
if __name__=='__main__':
    main()
