cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return ', '.join(str(i) for i in cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars[x][0] for x in cars]


def get_all_matching_models(cars=cars, grep='CO'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    car_list = []
    for i in cars:
        for model in cars[i]:
            if grep.lower() in model.lower():
                car_list.append(model)
    return sorted(car_list)


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    return {i:sorted(cars[i]) for i in cars}