"""
Iterate over the given names and countries lists. In each loop print the value of each and also the counter of the loop (starting at 1).

Here is the output you need to deliver. Ideally you use only one for loop.

The 2nd column should be exactly 10 chars wide aligning to the left (format magic):

       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico
"""


names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    fmt = '{}. {:<10} {}'
    for i, (name, country) in enumerate(zip(names, countries), 1):
        print(fmt.format(i, name, country))