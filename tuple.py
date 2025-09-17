
# tuple - immutable, faster than list, ordered, Read Only , can use tuple item as a key in dict

trip_summary = ("uber","chennai","airport",540.00,'completed')
print(trip_summary)

#access by index
print(trip_summary[1])

#loop
for item in trip_summary:
    print(item)

#legnth
print(len(trip_summary))

#count and index
print(trip_summary.count('completed'))
print(trip_summary.index('airport'))

#####SET##### unordered, uniion,diff,intersection
uber_cities = ["Chennai","Bangalore","chennai","delhi","Bangalore"]
uniq_cities = set(uber_cities)
print(uniq_cities)

uber_cities1 = {"Chennai","Mumbai","Bangalore"}
uber_cities2 = {"Delhi","Pune","Bangalore"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities1.difference(uber_cities2))
print(uber_cities2.difference(uber_cities1))

uber_cities1.add("karur")
print(uber_cities1)

uber_cities1.remove("Chennai")
print(uber_cities1)

my_set = {1,2,3}
my_set.remove(2)
print(my_set)
my_set.add(99)
print(my_set)
my_set.add(100)
print(my_set)
my_set.discard(100) #safe removal
my_set.add("sdsds")
print(my_set)