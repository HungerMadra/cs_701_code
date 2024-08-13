#Problem statement: Suppose a string variable season holds the current season, 
#a float variable temperature holds the current temperature, 
#and a boolean variable air_conditioner indicates if the air conditioner is on. Write a Python program that, 
#if the season is "summer", then if the temperature is above 72 it should set air_conditioner to True and 
#otherwise set it to False.

currentTemperature: float
airConditioner: bool
season = ("Spring", "Summer", "Fall", "Winter")

currentTemperature = float (input ("Please enter current temperature"))
enterSeason = input ("please enter season")

if enterSeason == "Summer" and currentTemperature >72:
    airConditioner = True
    print ("airConditioner On")
else :
    airConditioner = False
    print ("airConditioner Off")