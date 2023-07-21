# append()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.append("tesla")
print(cars)

#clear()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.clear()
print(cars)

# copy()
cars = ["buggati","ferrari","ford","rolls royce"]
carBrands = cars.copy()
print(carBrands)

# counjt()
cars = ["buggati","ferrari","ford","rolls royce","ford"]
f = cars.count("ford")
print(f)

# #extend()
cars = ["buggati","ferrari","ford","rolls royce"]
motors = ["toyota","gtr","nissan"]
cars.extend(motors)
print(cars)

# insert()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.insert(3,"corolla")
print(cars)


#pop()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.pop()
print(cars)

#remove()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.remove("ferrari")
print(cars)


#reverse()
cars = ["buggati","ferrari","ford","rolls royce"]
cars.reverse()
print(cars)


# sort()
cars = ["buggati","ferrari","ford","rolls royce", "gtr"]
cars.sort()
print(cars)


#index()
cars = ["buggati","ferrari","ford","rolls royce"]
b = cars.index("ford")
print(b)

