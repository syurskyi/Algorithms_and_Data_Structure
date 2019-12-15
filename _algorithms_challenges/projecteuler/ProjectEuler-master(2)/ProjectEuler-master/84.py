import collections
import random
import sys
        
class MonopolyOddsProblem():        
    def __init__(self):
        # Monopoly board
        self.n = 40
        self.board = [
            'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
            'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 
            'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
            'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2',  
        ]
        self.cc_cards = [i for i in range(1, 17)]
        self.cc_card_pos = 0
        self.cc_go_to_map = {
            1: 'GO',
            2: 'JAIL',
        }
        self.ch_cards = [i for i in range(1, 17)]
        self.ch_card_pos = 0
        self.ch_go_to_map = {
            1: 'GO',
            2: 'JAIL',
            3: 'C1',
            4: 'E3',
            5: 'H2',
            6: 'R1', 
        }
        self.ch_go_to_next_map = {
            7: { 'CH1': 'R2', 'CH2': 'R3', 'CH3': 'R1', }, 
            8: { 'CH1': 'R2', 'CH2': 'R3', 'CH3': 'R1', }, 
            9: { 'CH1': 'U1', 'CH2': 'U2', 'CH3': 'U1', }, 
        }
            
        # Player
        self.player_pos = 0
        self.consecutive_double_count = 0
        self.visited_counter = collections.Counter()
        
        # Helper
        self.inversed_board = {}
        for i in range(len(self.board)):
            self.inversed_board[self.board[i]] = i
        
        # Shuffle
        random.shuffle(self.cc_cards)
        random.shuffle(self.ch_cards)
        
    def simulate(self):
        for step in range(100000):
            x, y = self._use_dice()
            if self._has_three_consecutive_double(x, y):
                self._go_to_square('JAIL')
            self.player_pos = (self.player_pos + x + y) % self.n
            if self.board[self.player_pos] == 'G2J':
                self._go_to_square('JAIL')
            else:
                # CH3 may go back 3 squares to CC3
                if self.board[self.player_pos] in ['CH1', 'CH2', 'CH3']:
                    self._take_chance_card()    
                if self.board[self.player_pos] in ['CC1', 'CC2', 'CC3']:
                    self._take_community_chest_card()
            self.visited_counter[self.player_pos] += 1    

    def get_model_string(self):
        return ''.join(["%02d" % square[0] for square in self.visited_counter.most_common(3)])
        
    def _use_dice(self):
        return random.randint(1, 4), random.randint(1, 4)
        
    def _has_three_consecutive_double(self, x, y):
        if x == y:
            self.consecutive_double_count += 1
        else:
            self.consecutive_double_count = 0
        if self.consecutive_double_count == 3:
            self.consecutive_double_count = 0
            return True
        else:
            return False
    
    def _take_community_chest_card(self):
        assert(self.board[self.player_pos] in ['CC1', 'CC2', 'CC3'])
        card = self.cc_cards[self.cc_card_pos]
        if card in self.cc_go_to_map:
            self._go_to_square(self.cc_go_to_map[card])
        self.cc_card_pos = (self.cc_card_pos + 1) % 16
        
    def _take_chance_card(self):
        pos = self.board[self.player_pos]
        assert(pos in ['CH1', 'CH2', 'CH3'])
        card = self.ch_cards[self.ch_card_pos]
        if card in self.ch_go_to_map:
            self._go_to_square(self.ch_go_to_map[card])
        elif card in self.ch_go_to_next_map:
            self._go_to_square(self.ch_go_to_next_map[card][pos])
        elif card == 10:
            self.player_pos = (self.player_pos - 3 + self.n) % self.n
        self.ch_card_pos = (self.ch_card_pos + 1) % 16
    
    def _go_to_square(self, square):
        self.player_pos = self.inversed_board[square]
    
def main():
    problem = MonopolyOddsProblem()
    problem.simulate()
    print(problem.get_model_string())
    
if __name__ == '__main__':
    sys.exit(main())
