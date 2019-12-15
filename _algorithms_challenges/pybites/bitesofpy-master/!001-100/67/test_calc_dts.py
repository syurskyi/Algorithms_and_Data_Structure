from calc_dts import (get_hundred_days_end_date,
                      get_days_between_pb_start_first_joint_pycon)


def test_get_hundred_days_end_date():
    assert get_hundred_days_end_date() == '2017-07-08'


def test_get_days_till_pycon_meetup():
    assert get_days_between_pb_start_first_joint_pycon() == 505