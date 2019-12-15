from coursetime import get_all_timestamps, calc_total_course_duration


def test_get_all_timestamps():
    timestamps = get_all_timestamps()
    assert len(timestamps) == 99
    assert '2:29' in timestamps
    assert '4:19' in timestamps
    assert '6:06' in timestamps
    assert '8:39' in timestamps


def test_calc_total_course_duration():
    timestamps = get_all_timestamps()
    assert '6:50:31' in calc_total_course_duration(timestamps)