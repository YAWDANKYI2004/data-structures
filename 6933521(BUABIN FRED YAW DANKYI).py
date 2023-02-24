#github.com/YAWDANKYI2004
#list of available cars and their prices
cars={"  Range Rover Sport L320":40200,
      "AC Frua":50320,
      "AC 3000ME":32000,
      "AC/Shelby Cobra":60500,
      "Alfa Romeo 7":35555,
      "Alfa Romeo 33":27888,
      "Alfa Romeo 33 Stradale":90000,
      "Audi A3":70400,
      "Audi A4":43444,
      "Audi R8":55545,
      "BMW 326":22334,
      "Lagonda 16/80":122222,
      "Lagonda 3-litre":34345,
      "Lamborghini 400GT":345345,
      "Lamborghini Aventador":1122334,
      "Lamborghini Countach":3322111,
      "Lamborghini Diablo":550000,
      "  Lamborghini Espada":2000000,
      "Mercedes-Benz Type 300 Adenauer":70000,
      "Mercedes-Benz C-Class":56666,
      "Mercedes-AMG GT":600000,
      "Mercedes-AMG T":545454,
      "Mitsubishi Outlander P-HEV":121212,
      "Nissan Leaf":300000,
      "Opel Vectra":200000,
      "Opel Corsa":299999,
      "Opel Astra":455535,
      "Buabin model":451235,}
# get user input for car name
car_name=input("Enter a car_name.")
#check if car name is in the list of available cars
if car_name in cars:
     print("Yes")
     #if car name is present,get its price
     car_price=cars[car_name]
     print( f"The price of {car_name} is ${car_price}." )
else:
    # if car name is not present, inform the user
    print(f"Sorry,{car_name} is not available.")