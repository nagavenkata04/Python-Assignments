# WRITE YOUR CODE HERE
def area_rectangle_1(length, width):
    area = length * width
    s = round(area,2)
    return s

def surface_area(radius):
    import math
    PI = math.pi
    # surface_area_sphere Formula
    surface_area = 4 * PI * radius ** 2
    A = round(surface_area, 2)
    return A

def volume_sphere(radius):
    import math
    PI = math.pi
    # Volume_sphere Formula
    volume_sphere = (4/3) * PI * radius ** 3 
    volume_sphere = round(volume_sphere, 2)
    return volume_sphere

def bmi(weight, height):
    # bmi Formula 
    bmi = weight * 703 / height ** 2
    bmi = round(bmi, 2)
    return bmi

def refund(no_one_liter_bottles, no_more_than_one_liter_bottles):
    no_one_liter_bottles = no_one_liter_bottles * 0.10
    no_more_than_one_liter_bottles = no_more_than_one_liter_bottles * 0.25
    refund = no_more_than_one_liter_bottles + no_one_liter_bottles
    refund = round(refund, 2)
    return refund

def simple_interest(P,r,t):
    # Principal : P
    # rate : r
    # time : t
    # simple_interest : A
    r = r/100
    A = P * (1 + r * t)
    A = round(A, 2)
    return A

def compound_interest(P,r,t,n):
    # Principal Amount : P
    # AnnuaL rate of Interest : r
    # number of years the amount is invested : t
    #  number of times the interest is compounded per year: n
    r = r / 100
    compound_interest = P * pow((1 + r/n), n * t)
    compound_interest = round( compound_interest, 2)
    return compound_interest

def welcome_user(name):
    g = f"Hello, {name}, nice to meet you!"
    return g 

def values(x, y, z):
    return f"The value of x is: {x}.\n"f"The value of y is: {y}.\n"f"The value of z is: {z}."

def area_rectangle_2(length, width):
    #Area of Rectangle with F String
    area = round(length * width, 2)
    return f"The area of a rectangle with length {length} and width {width} is {area}."

def results(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a//b
    remainder = a % b
    power = a**b
    return f"The sum of {a} and {b} is {sum}.\n"f"The difference when {b} is subtracted from {a} is {difference}.\n"f"The product of {a} and {b} is {product}.\n"f"The quotient when {a} is divided by {b} is {quotient}.\n"f"The remainder when {a} is divided by {b} is {remainder}.\n"f"The result of {a}^{b} is {power}."

def simple_interest_2(P,r,t):
    # Principal : P
    # rate : r
    # time : t
    # simple_interest : A
    A = P * (1 + (r/100) * t)
    A = round(A, 2)
    return f'After {t} years at {r}%, the investment will be worth ${A:.2f}.'

def compound_interest_2(P,r,t,n):
    # Principal Amount : P
    # AnnuaL rate of Interest : r
    # number of years the amount is invested : t
    #  number of times the interest is compounded per year: n
    A = P * pow((1 + (r/100)/n), n * t)
    A = round( A, 2)
    investment = f'${P} invested at {r}% for {t} years compounded {n} times per year is ${A:.2f}.'
    return investment

def count_characters(input_string):
    number_of_characters = len(input_string)
    input_char_count = f"The input string '{input_string}' has {number_of_characters} characters."
    return input_char_count

def ad_lib(noun, verb, adjective, adverb):
    sentence = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    return sentence

def retirement(current_age, age_at_retirement, current_year):
    years_left = age_at_retirement - current_age
    retirement_year = current_year + years_left   
    return f"Your current age is: {current_age}.\nYou would like to retire at: {age_at_retirement}.\nYou have {years_left} years left until you can retire.\nIt's {current_year}, so you can retire in {current_year + years_left}."

def dimension(length, width):
    area1 = length * width
    area2 = area1 *0.09290304
    return f"The length of the room in feet is {length}.\nThe width of the room in feet is {width}.\nThe dimension of the room is {length} by {width} feet.\nThe area is\n{length * width} square feet\n{area2:.2f} square meters"

def pizza(number_of_people, number_of_pizzas):
    num_of_slices = (number_of_pizzas*8) // number_of_people
    leftover = (number_of_pizzas*8)%number_of_people
    return f"There are {number_of_people} people with {number_of_pizzas} pizzas.\nEach person gets {num_of_slices} pieces of pizza.\nThere are {leftover} leftover pieces."

import math
def paint(length, width):
    ga = math.ceil((length * width)/350)
    return f"You will need to purchase {ga} gallons of paint to cover {math.ceil(length*width)} square feet."

def fstring1(k):
    return f"The value is: {k:.4f}."

def fstring2(k):
    ans = f"{k:.4f}"
    return f"The value is: {ans:>10}."

def fstring3(k):
    value1 = f"{k:.6f}"
    return f"The value is: {value1:-<10}."

def fstring4(k):
    value_string_4 = f"{k:.6f}"
    return f"The value is: {value_string_4:-^12}."

