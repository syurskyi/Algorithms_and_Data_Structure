import pytest

from Previous.stats import BiteStats


@pytest.fixture(scope="module")
def bite_stats():
    return BiteStats()


def test_number_bites_accessed(bite_stats):
    assert bite_stats.number_bites_accessed == 176


def test_number_bites_resolved(bite_stats):
    assert bite_stats.number_bites_resolved == 115


def test_number_users_active(bite_stats):
    assert bite_stats.number_users_active == 114


def test_number_users_solving_bites(bite_stats):
    assert bite_stats.number_users_solving_bites == 76


def test_top_bite_by_number_of_clicks(bite_stats):
    assert int(bite_stats.top_bite_by_number_of_clicks) == 101


def test_top_user_by_bites_completed(bite_stats):
    assert bite_stats.top_user_by_bites_completed == 'mcaberasu'