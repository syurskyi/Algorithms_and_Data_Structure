c_ HashTable o..

    ___ -
        size _ 10
        keys _ [N..] * size
        values _ [N..] * size

    ___ put key, data

        index _ hashfunction(key)

        # not None -> it is a collision !!!
        _____ keys[index] __ n.. N..
            __ keys[index] __ key:
                values[index] _ data  # update
                r_

            # rehash try to find another slot
            index _ (index + 1) % size

        # insert
        keys[index] _ key
        values[index] _ data

    ___ get key

        index _ hashfunction(key)

        _____ keys[index] __ n.. N..
            __ keys[index] __ key:
                r_ values[index]

            index _ (index + 1) % size

        # it means the key is not present in the associative array
        r_ N..

    ___ hashfunction key
        sum _ 0
        ___ pos __ r..(l..(key
            sum _ sum + ord(key[pos])

        r_ sum % size


__ __name__ __ "__main__":
    table _ HashTable()

    table.put("apple", 10)
    table.put("orange", 20)
    table.put("car", 30)
    table.put("table", 40)

    print(table.get("cara"))
