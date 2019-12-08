# Example code to find index associated with a key using the
# enumerate function

records = [ ('mashrur@example.com','Hello world'),
            ('johndoe@example.com','Hello to you too'),
            ('janedoe@example.com','Python is awesome')
            ]

for index, record in enumerate(records):
    key, value = record
    if key == "johndoe@example.com":
        break

print(records[index])
