# City Name

def city_country(city, country):
    """print City and Country"""

    Name = city + ' ' + country
    return Name.title()

cc = {"santiago":"chile", "kandy":"sri lanka", "NYC":"USA"}

for i in cc:
    final_name = city_country(i, cc[i])
    print(final_name)

