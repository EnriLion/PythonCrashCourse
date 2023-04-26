def make_car(manufacturer, model, **car_info):
    """Function to receive a manufacturer  a car  model name"""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

cat = make_car('subaru', 'outback', color='blue', tow_package=True)

print(cat)
