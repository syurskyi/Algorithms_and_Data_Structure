import sys

spell_map = {
    0: '',
    1: 'one',
    2: 'two', 
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six', 
    7: 'seven', 
    8: 'eight', 
    9: 'nine', 
    10: 'ten', 
    11: 'eleven', 
    12: 'twelve', 
    13: 'thirteen', 
    14: 'fourteen', 
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen', 
    18: 'eighteen',
    19: 'nineteen', 
    20: 'twenty', 
    30: 'thirty',
    40: 'forty', 
    50: 'fifty', 
    60: 'sixty', 
    70: 'seventy', 
    80: 'eighty', 
    90: 'ninety', 
    100: 'hundred',
    1000: 'thousand',
}

def word_len(n):
    if n < 20:
        return len(spell_map[n])
    if n < 100:
        return len(spell_map[n % 10]) + len(spell_map[int(n/10) * 10])
    if n < 1000:
        return len(spell_map[100]) + len(spell_map[int(n/100)]) + (0 if n % 100 == 0 else 3) + word_len(n % 100);
    return len(spell_map[1]) + len(spell_map[1000]) 
    
def main():    
    sum = 0
    for n in range(1, 1001):
        sum += word_len(n)
    print(sum)
    
if __name__ == '__main__':
    sys.exit(main())
