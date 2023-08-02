#removing
cars = ["bugatti","tesla","GTR","lumborginhi","ferrari"]
cars.remove("ferrari")
cars.remove("tesla")
print(cars)



#adding
cars = ["bugatti","tesla","GTR","lumborginhi","ferrari"]
cars.insert(2,"toyota")
cars.insert(0,"jeep")
print(cars)


#access
cars = ["bugatti","tesla","GTR","lumborginhi","ferrari"]
print(cars[0])
print(cars[1])
print(cars[-1])
print(cars[-2])

#change 
cars = ["bugatti","tesla","GTR","lumborginhi","ferrari"]
cars[1]="supra"
cars[-1]="bumblebee"
print(cars)