from itertools import combinations, permutations

def friends_teams(friend_list: list, team_size: int, order_does_matter: bool = False) -> list:
    if order_does_matter:
        return [x for x in permutations(friend_list,team_size)]
    else:
        return [x for x in combinations(friend_list,team_size)]
