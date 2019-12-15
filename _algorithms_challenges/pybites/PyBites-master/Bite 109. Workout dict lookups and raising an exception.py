"""
You are presented with workout_schedule with keys: days and values: workouts. Complete get_workout_motd that 
receives a day string, title case it so the function can receive case insensitive days, look it up in the 
dict and do two things:

If the day (key) is not in the dictionary, raise a KeyError, we don't want this function to continue, the 
caller needs to catch this exception,
If the key is in the dictionary, return chill or go_train depending if it's a Rest day or not. The latter
 you will need to string-interpolate using format.
"""

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}

rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    day = str(day.capitalize())
    try:
        if workout_schedule[day] == rest:
            return chill
        elif workout_schedule[day] != 'Rest':
            return go_train.replace('{}', workout_schedule[day])
    except KeyError:
        raise
