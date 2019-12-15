from bmi import person_max_bmi, data


def test_person_max_bmi():
    assert person_max_bmi() == ('Yoda', 39.03)


def test_person_max_bmi_smaller_dataset():
    newdata = '\n'.join(data.splitlines()[:10])
    assert person_max_bmi(newdata) == ('Owen Lars', 37.87)


def test_person_max_bmi_another_smaller_dataset():
    newdata = '\n'.join([row for row in data.splitlines()
                         if row.lstrip()[:4] not in ('Owen', 'Yoda')])
    assert person_max_bmi(newdata) == ('IG-88', 35.0)