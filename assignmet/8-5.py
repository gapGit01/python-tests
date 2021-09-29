def describe_city(city, country):
    """ Details about the city"""

    print (f"\n{city} is in {country}\n")


c = {'dhili':'insia', 'tokyo':'japan', 'kandy':'sri lanka'}

for i in c:
     describe_city(i, c[i])
