#Dictionary - Key value pair - duplicate not allowed
trip = {
    "trip-id" : "UB123",
    "pickup" : "Chennai",
    "drop" : ["Airport","Tambaram","Medavakkam"],
    "fare" : 540.00,
    "driver": "Ravi",
    "status" : "Completed"
}

'''
print(trip["driver"])

print(trip.get("pickup"))
print(trip.keys())
print(trip.values())
'''
#Iterate
for key,val in trip.items():
    print(key,val)

#Update
trip.update({"car_model" : "suzuki"})
print(trip)

#pop
trip.pop("status")
print(trip)

# accessing one item from the list 
print(trip["drop"][1])
#accessing all items from a single key
for loca in trip["drop"]:
    print(loca)

trips = [
{
    "trip-id" : "UB123",
    "pickup" : "Chennai",
    "drop" : ["Airport","Tambaram","Medavakkam"],
    "fare" : 540.00,
    "driver": "Ravi",
    "status" : "Completed"
},
{
    "trip-id" : "UB1234",
    "pickup" : "Bangalore",
    "drop" : ["Airport","XXX","YY"],
    "fare" : 1540.00,
    "driver": "Rahim",
    "status" : "Completed"
},
{
    "trip-id" : "UB1235",
    "pickup" : "Trichy",
    "drop" : ["Airport","Tolgate","Musiri"],
    "fare" : 1040.00,
    "driver": "Shan",
    "status" : "Completed"
}
]

#print(trips)
print(trips[1])
print(trips[1].keys())
print(trips[2]["fare"])

for trip in trips:
    print(trip["driver"])


