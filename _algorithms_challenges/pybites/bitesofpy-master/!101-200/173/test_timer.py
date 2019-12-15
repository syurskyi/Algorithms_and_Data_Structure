from timer import add_todo


def test_wash_car_tomorrow_morning():
    actual = add_todo("11h 10m", "Wash my car")
    expected = "Wash my car @ 2019-02-07 09:10:00"
    assert actual == expected


def test_code_bite_tomorrow_same_time():
    actual = add_todo("30d", "Code a Bite")
    expected = "Code a Bite @ 2019-03-08 22:00:00"
    assert actual == expected


def test_go_to_bed_in_five_min_and_three_seconds():
    actual = add_todo("5m 3s", "Go to Bed")
    expected = "Go to Bed @ 2019-02-06 22:05:03"
    assert actual == expected


def test_finish_this_test_in_seconds_as_int():
    actual = add_todo("45", "Finish this Test")
    expected = "Finish this Test @ 2019-02-06 22:00:45"
    assert actual == expected


def test_study_data_science_at_d_h_m_s():
    actual = add_todo("1d 10h 47m 17s", "Study some Python")
    expected = "Study some Python @ 2019-02-08 08:47:17"
    assert actual == expected