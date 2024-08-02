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
# Defining the required funtions in this module

# Computing area of white-washing
def whitewashing_area(l,b,h):
    """
    function to calculate whitewashing area
    para:
        l - int/float - length
        b - int/float - width/breath
        h - int/float - height
    return type: float/int area of whitewashing
    """
    return 2*h*(l+b) + (l*b)

# Computing the cost of white-washing
def whitewashing_cost(area, rate_per_sq_feet=15):
    """
    function to calculate whitewashing cost
    para:
        area - int/float - area
        rate_per_sq_feet - int/float - default - 15
    return type: float/int cost of whitewashing
    """
    return area*rate_per_sq_feet

# Computing the 
def flooring_cost(l,w,mosaic_rate=100, cement_rate=55):
    """
    function to calculate cost of flooring
    para:
        l - int/float - length
        w - int/float - width/breath
        mosaic_rate - int/float - cost of mosaic flooring - def:100
        cement_rate - int/float - cost of cement flooring - def:55
    return type: float/int cost of flooring
    """
    return mosaic_rate*l*w,cement_rate*l*w

def display_costs(l,w,h):
     """
    function to calculate all and display
    para:
        l - int/float - length
        w - int/float - width/breath
        h - int/float - height
    return type: None
    """
    w_a = whitewashing_area(l,w,h)
    w_c = whitewashing_cost(w_a)
    mosaic,cement = flooring_cost(l,w)
    print(f"White Washing Cost: {w_c:.2f} \nFlooring Cost: Mosaic:{mosaic:.2f}  Cement:{cement:.2f}")
