from Previous.nba import (cur,
                          player_with_max_points_per_game,
                          number_of_players_from_duke,
                          avg_years_active_players_stanford,
                          year_with_most_drafts)


def test_total_row_count_after_import():
    sql = '''SELECT COUNT(*) FROM players'''
    cur.execute(sql)
    ret = cur.fetchall()
    assert ret[0][0] == 3961


def test_player_with_max_points_per_game():
    assert player_with_max_points_per_game() == 'Michael Jordan'


def test_number_of_players_from_duke():
    assert number_of_players_from_duke() == 58


def test_avg_years_active_players_stanford():
    assert round(avg_years_active_players_stanford(), 2) == 4.58


def test_year_with_most_drafts():
    assert int(year_with_most_drafts()) == 1984