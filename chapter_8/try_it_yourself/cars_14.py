# 8-14. Cars:   Write a function that stores informaton about a car in a dictionary.
#               The function should always receive a manufacturer and a model name.
#               It should then accept an arbitary number of keyword arguments. Call the
#               function with the required information and two other name-value pairs, such
#               as a color or an optional feature. Your function should work for a call like this one:
#
#               car = make_car('subaru', 'outback', colour='blue', tow_package=True)
#
#               Print the dictionary that's returned to make sure all the informaton was stored correctly.


def car_stock(manufacturer, model, **car_info):
    """Create a dictionary about every car in stock"""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

car_profile = car_stock('subaru', 'outback',
                          colour='blue',
                          tow_package=True,)

print(car_profile)
