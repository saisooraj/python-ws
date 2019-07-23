"""Program to calculate trip cost for the given number of people"""
no_of_persons = int(input("enter the no. of persons:"))
distance_km = int(input("enter the distance in KM:"))
milage_km = int(input("enter the milage in KM:"))
fuel_price = int(input("enter the fuel price:"))

no_litres_used = distance_km / milage_km
total_cost = no_litres_used * fuel_price
price_per_head = total_cost / no_of_persons
print(f"Total cost per person is :{price_per_head}")