from friends import get_friend_with_most_friends, friendships


def test_default_friendships_list():
    user, friends = get_friend_with_most_friends(friendships)
    assert user == 'sara'
    assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']


def test_different_friendships_list():
    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    user, friends = get_friend_with_most_friends(friendships)
    assert user == 'joyce'
    assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
                                     'rod', 'sara']


def test_friendships_list_with_duplicate_names():
    names = 'bob bob tim tim julian julian'.split()
    ids = range(len(names))
    users = dict(zip(ids, names))

    friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3),
                   (2, 4), (4, 5)]
    user, friends = get_friend_with_most_friends(friendships, users=users)
    assert user == 'bob'
    assert sorted(list(friends)) == ['bob', 'julian', 'julian', 'tim']