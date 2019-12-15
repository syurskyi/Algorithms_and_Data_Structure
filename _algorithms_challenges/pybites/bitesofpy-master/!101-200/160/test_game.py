import pytest

from Previous.game import get_winner

PLAYERS = ("Rock Gun Lightning Devil Dragon Water Air Paper Sponge "
           "Wolf Tree Human Snake Scissors Fire").split()


@pytest.mark.parametrize("args", [('Rock', 'blabla'),
                                  ('blabla', 'Rock')])
def test_bad_inputs(args):
    with pytest.raises(ValueError):
        get_winner(*args)


@pytest.mark.parametrize("player", PLAYERS)
def test_ties(player):
    assert get_winner(player, player) == 'Tie'


# all 105 outcomes
# http://www.umop.com/rps15.htm

def test_rock_pounds_out_fire():
    assert get_winner('Rock', 'Fire') == 'Rock'


@pytest.mark.parametrize("player", ['Scissors', 'Snake', 'Human',
                                    'Wolf', 'Sponge'])
def test_rock_crushes_scissors_snake_human_wolf_and_sponge(player):
    assert get_winner('Rock', player) == 'Rock'


def test_rock_blocks_growth_of_tree():
    assert get_winner('Rock', 'Tree') == 'Rock'


def test_fire_melts_scissors():
    assert get_winner('Fire', 'Scissors') == 'Fire'


@pytest.mark.parametrize("player", ['Paper', 'Snake', 'Human',
                                    'Tree', 'Wolf', 'Sponge'])
def test_fire_burns_paper_snake_human_tree_wolf_and_sponge(player):
    assert get_winner('Fire', player) == 'Fire'


def test_scissors_swish_through_air():
    assert get_winner('Scissors', 'Air') == 'Scissors'


def test_scissors_carve_tree():
    assert get_winner('Scissors', 'Tree') == 'Scissors'


@pytest.mark.parametrize("player", ['Paper', 'Snake', 'Human',
                                    'Wolf', 'Sponge'])
def test_scissors_cut_paper_snake_human_wolf_and_spnge(player):
    assert get_winner('Scissors', player) == 'Scissors'


@pytest.mark.parametrize("player", ['Human', 'Wolf'])
def test_snake_bites_human_and_wolf(player):
    assert get_winner('Snake', player) == 'Snake'


def test_snake_swallows_sponge():
    assert get_winner('Snake', 'Sponge') == 'Snake'


@pytest.mark.parametrize("player", ['Tree', 'Paper'])
def test_snake_nests_in_tree_and_paper(player):
    assert get_winner('Snake', player) == 'Snake'


def test_snake_breathes_air():
    assert get_winner('Snake', 'Air') == 'Snake'


def test_snake_drinks_water():
    assert get_winner('Snake', 'Water') == 'Snake'


def test_human_plants_tree():
    assert get_winner('Human', 'Tree') == 'Human'


def test_human_tames_wolf():
    assert get_winner('Human', 'Wolf') == 'Human'


def test_human_cleans_with_sponge():
    assert get_winner('Human', 'Sponge') == 'Human'


def test_human_writes_paper():
    assert get_winner('Human', 'Paper') == 'Human'


def test_human_breathes_air():
    assert get_winner('Human', 'Air') == 'Human'


def test_human_drinks_water():
    assert get_winner('Human', 'Water') == 'Human'


def test_human_slays_dragon():
    assert get_winner('Human', 'Dragon') == 'Human'


@pytest.mark.parametrize("player", ['Wolf', 'Dragon'])
def test_tree_shelters_wolf_and_dragon(player):
    assert get_winner('Tree', player) == 'Tree'


def test_tree_outlives_sponge():
    assert get_winner('Tree', 'Sponge') == 'Tree'


def test_tree_becomes_paper():
    assert get_winner('Tree', 'Paper') == 'Tree'


def test_tree_produces_air():
    assert get_winner('Tree', 'Air') == 'Tree'


def test_tree_drinks_water():
    assert get_winner('Tree', 'Water') == 'Tree'


def test_tree_imprisons_devil():
    assert get_winner('Tree', 'Devil') == 'Tree'


@pytest.mark.parametrize("player", ['Sponge', 'Paper'])
def test_wolf_chews_up_sponge_and_paper(player):
    assert get_winner('Wolf', player) == 'Wolf'


def test_wolf_breathes_air():
    assert get_winner('Wolf', 'Air') == 'Wolf'


def test_wolf_drinks_water():
    assert get_winner('Wolf', 'Water') == 'Wolf'


@pytest.mark.parametrize("player", ['Dragon', 'Lightning'])
def test_wolf_outruns_dragon_and_lightning(player):
    assert get_winner('Wolf', player) == 'Wolf'


def test_wolf_bites_devils_heiny():
    assert get_winner('Wolf', 'Devil') == 'Wolf'


def test_sponge_soaks_paper():
    assert get_winner('Sponge', 'Paper') == 'Sponge'


def test_sponge_uses_air_pockets():
    assert get_winner('Sponge', 'Air') == 'Sponge'


def test_sponge_absorbs_water():
    assert get_winner('Sponge', 'Water') == 'Sponge'


@pytest.mark.parametrize("player", ['Devil', 'Dragon'])
def test_sponge_cleanses_devil_and_dragon(player):
    assert get_winner('Sponge', player) == 'Sponge'


def test_sponge_cleans_guns():
    assert get_winner('Sponge', 'Gun') == 'Sponge'


def test_sponge_conducts_lightning():
    assert get_winner('Sponge', 'Lightning') == 'Sponge'


def test_paper_fans_air():
    assert get_winner('Paper', 'Air') == 'Paper'


def test_paper_covers_rock():
    assert get_winner('Paper', 'Rock') == 'Paper'


def test_paper_floats_on_water():
    assert get_winner('Paper', 'Water') == 'Paper'


@pytest.mark.parametrize("player", ['Devil', 'Dragon'])
def test_paper_rebukes_devil(player):
    assert get_winner('Paper', player) == 'Paper'


def test_paper_outlaws_gun():
    assert get_winner('Paper', 'Gun') == 'Paper'


def test_paper_defines_lightning():
    assert get_winner('Paper', 'Lightning') == 'Paper'


def test_air_blows_out_fire():
    assert get_winner('Air', 'Fire') == 'Air'


def test_air_erodes_rock():
    assert get_winner('Air', 'Rock') == 'Air'


def test_air_evaporates_water():
    assert get_winner('Air', 'Water') == 'Air'


def test_air_chokes_devil():
    assert get_winner('Air', 'Devil') == 'Air'


def test_air_tarnishes_gun():
    assert get_winner('Air', 'Gun') == 'Air'


def test_air_freezes_dragon():
    assert get_winner('Air', 'Dragon') == 'Air'


def test_air_creates_lightningj():
    assert get_winner('Air', 'Lightning') == 'Air'


@pytest.mark.parametrize("player", ['Devil', 'Dragon'])
def test_water_drowns_devil_and_dragon(player):
    assert get_winner('Water', player) == 'Water'


def test_water_erodes_rock():
    assert get_winner('Water', 'Rock') == 'Water'


def test_water_puts_out_fire():
    assert get_winner('Water', 'Fire') == 'Water'


@pytest.mark.parametrize("player", ['Scissors', 'Gun'])
def test_water_rusts_scissors_and_gun(player):
    assert get_winner('Water', player) == 'Water'


def test_water_conducts_lightning():
    assert get_winner('Water', 'Lightning') == 'Water'


def test_dragon_commands_devil():
    assert get_winner('Dragon', 'Devil') == 'Dragon'


@pytest.mark.parametrize("player", ['Lightning', 'Fire'])
def test_dragon_breathes_lightning_and_fire(player):
    assert get_winner('Dragon', player) == 'Dragon'


def test_dragon_rests_on_rock():
    assert get_winner('Dragon', 'Rock') == 'Dragon'


@pytest.mark.parametrize("player", ['Scissors', 'Gun'])
def test_dragon_is_immune_to_scissors_and_gun(player):
    assert get_winner('Dragon', player) == 'Dragon'


def test_dragon_spawns_snake():
    assert get_winner('Dragon', 'Snake') == 'Dragon'


def test_devil_hurls_rocks():
    assert get_winner('Devil', 'Rock') == 'Devil'


def test_devil_breaths_fire():
    assert get_winner('Devil', 'Fire') == 'Devil'


@pytest.mark.parametrize("player", ['Scissors', 'Gun'])
def test_devil_is_immune_to_scissors_and_gun(player):
    assert get_winner('Devil', player) == 'Devil'


def test_devil_casts_lightning():
    assert get_winner('Devil', 'Lightning') == 'Devil'


def test_devil_eats_snake():
    assert get_winner('Devil', 'Snake') == 'Devil'


def test_devil_possesses_human():
    assert get_winner('Devil', 'Human') == 'Devil'


@pytest.mark.parametrize("player", ['Gun', 'Scissors'])
def test_lightning_melts_gun_and_scissors(player):
    assert get_winner('Lightning', player) == 'Lightning'


@pytest.mark.parametrize("player", ['Rock', 'Tree'])
def test_lightning_splits_rocks_and_trees(player):
    assert get_winner('Lightning', player) == 'Lightning'


def test_lightning_starts_fire():
    assert get_winner('Lightning', 'Fire') == 'Lightning'


@pytest.mark.parametrize("player", ['Snake', 'Human'])
def test_lightning_strikes_snake_and_human(player):
    assert get_winner('Lightning', player) == 'Lightning'


@pytest.mark.parametrize("player", ['Rock', 'Tree', 'Fire'])
def test_gun_targets_rock_tree_and_fire(player):
    assert get_winner('Gun', player) == 'Gun'


def test_gun_outclasses_scissors():
    assert get_winner('Gun', 'Scissors') == 'Gun'


@pytest.mark.parametrize("player", ['Snake', 'Human', 'Wolf'])
def test_gun_shoots_snake_human_and_wolf(player):
    assert get_winner('Gun', player) == 'Gun'