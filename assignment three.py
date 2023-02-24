#Index number 6940921
#This code belongs to Lartey Sussana Legol
#This code is used to attain enquires of car models and their prices
carModels = {
    "Hyndai Mighty":139300,
    "Mercedes-Benz c":163450,
    "Suzuki S-presso GL":173904,
    "Nissan Navara":459250,
    "Lexus LX 570":1958650,
    "Toyota Fortuber":756250,
    "Toyota Coaster":846850,
    "Nissan Patrol LE":990556,
    "Mitsubishi Outlander GLX":567131,
    "Mitsubishi Eclipse Cross 4x4":516859,
    "Scania R460 A6X4NZ ADR(Art Head)":1461430,
    "Toyota Landcruiser prado TX.L":449050,
    "Mazda 2":58000,
    "Kia Rhino":209350,
    "Honda Civic":158350,
    "Hyundai Santa Fe":214450,
    "Toyota Highlander":306250,
    "BMW 535":479650,
    "Mercedes Benz C-Class":300000,
    "Kia Sportage":92000,
    "Ford F-150":400000,
    "Chrystler Pacific Hybrid":500000,
    "Porsche 911":1000000,
    "Dodge Challenger":469900,
    "Chevrolet Camaro":414990,
    "Hyndai Elantra":200000,
    "Porsche Macan":525677,
    "Audi Q7":610000,
    "Bugatti La Voiture Noire":5900000,
    "Lamborghini Venemo":6000000 }
carModel =input("Enter car model of your choice: ")
if carModel in carModels:
    print("Available")
    carPrice = carModels[carModel] 
    print(f"The price of {carModel} is ${carPrice}") 
else:
    #if unavailable inform the customer
    print(f"{carModel} is not available")




    
    
    
    
    
    
    