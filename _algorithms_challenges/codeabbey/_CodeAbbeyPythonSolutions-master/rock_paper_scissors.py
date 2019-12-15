amount_values = int(input())
results = []

def get_round_winner(player1, player2):
    player1_move = ord(player1)
    player2_move = ord(player2)
    if(player1_move < player2_move):
        if(player1_move - player2_move < -2):
            return 2
        return 1
    elif(player1_move > player2_move):
        if(player1_move - player2_move > 2):
            return 1
        return 2
    else:
        return 0


def get_match_winner(moves):
    player_1_result = 0
    player_2_result = 0
    for i in moves:
        round_winner = get_round_winner(i[0], i[1])
        if(round_winner == 1):
            player_1_result += 1
        elif(round_winner == 2):
            player_2_result += 1

    if(player_1_result > player_2_result):
        return 1
    elif(player_2_result > player_1_result):
        return 2
    else:
        return 0
    
for i in range(amount_values):
    moves = list(map(str, input().split()))
    results.append(get_match_winner(moves))

print(*results)