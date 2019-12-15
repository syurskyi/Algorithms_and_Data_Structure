from medals import data, athletes_most_medals


def test_athletes_most_medals_default_csv():
    ret = athletes_most_medals()
    assert len(ret) == 2
    assert ret["LATYNINA, Larisa"] == 18
    assert ret["PHELPS, Michael"] == 22


def test_smaller_csv_and_guarantee_checking_male_and_female():
    ret = athletes_most_medals(
        data.replace('summer', 'summer_2008-2012')
    )
    assert len(ret) == 2
    assert ret["PHELPS, Michael"] == 14
    assert ret["COUGHLIN, Natalie"] == 7  # not LOCHTE, Ryan