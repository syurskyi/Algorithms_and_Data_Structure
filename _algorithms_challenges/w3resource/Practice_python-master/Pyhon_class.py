import math

# 1, 2
class roman_integer:
    roman = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
             ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10),
             ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))

    def int_to_roman(self, num):
        """" converts a number to a roman numeral """
        result = ''
        for integer in self.roman:
            while True:
                if num >= integer[1]:
                    result += integer[0]
                    num -= integer[1]
                else:
                    break
        return result

    def roman_to_int(self, cs):
        # MMMMCDXLVIII
        """converts a roman numeral to a normal number """
        num = 0
        roman_dict = dict(self.roman)
        for letter in range(len(cs)):
            if letter > 0 and roman_dict[cs[letter]] > roman_dict[cs[letter - 1]]:
                num += roman_dict[cs[letter]] - 2 * roman_dict[cs[letter - 1]]
            else:
                num +=roman_dict[cs[letter]]
        return num    


# print(roman_integer().int_to_roman(4448))
# print(roman_integer().roman_to_int("MMMMCDXLVIII"))


# 3
class proper_parenteses:
    parenteses = {"(": ")", "[": "]", "{": "}"}
    def parenteses_validator(self, string):
        """checks to see if the parenteses are valid occording to
        python standards. Returns False if not valid or no type of
        parenteses like (), {}, []
        """
        begin = ''
        string_list = list(string)
        if len(string_list) <= 1:
            return False
        while len(string_list) > 1:
            if "]" in string_list or "}" in string_list or ")" in string_list:
                for letter in string_list:
                    if letter == "(" or letter == "[" or letter == "{":
                        begin = letter
                    elif letter == ")" or letter == "]" or letter == "}":
                        if letter != self.parenteses[begin]:
                            return False
                        else:
                            string_list.remove(begin)
                            string_list.remove(letter)
                            continue
            else:
                return False
        return True


# print(proper_parenteses().parenteses_validator("0"))


# 4
class subsets:
    listed = [[]]
    def sub_sets(self, sset):  
        return self.subsetsRecur([], sorted(sset))  
      
    def subsetsRecur(self, current, sset):  
        if sset:  
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])  
        return [current]  
  
# print(subsets().sub_sets([4,5,6]))


# 7
class Power:
    def power(self, x, y):
        """ returns x to the power of y."""
        if x == 1 or y == 0:
            return 1
        elif x < 0 or isinstance(y, int) == False:
            raise ValueError
        else:
            z = 1
            for num in range(y):
                z = float(z) * float(x)
            return round(z, 2)


# print(Power().power(2.23, 4))



# 8
class reverseWords:
    def reverse_words(self, sentence):
        """ reverses the order of a sentence so it reads backwards """
        reversed_sentence = sentence.split()
        reversed_sentence= reversed(reversed_sentence)
        return ' '.join(reversed_sentence)


# print(reverseWords().reverse_words("hello .py nuzzz whats up"))


# 9
class Strings:
    def get_string(self):
        """ recieves a string from a user """
        string = input("Please give a string:  ")
        return string

    def print_string(self):
        """ returns a string given in uppercase """
        return self.get_string().upper()


# print(Strings().print_string())


#  10
class Rectangle:
#     length = input("Length:  ")
#     width = input("Height:  ")

    def area_rectangle(self):
        """returns area of rectangle """
        return int(self.length) * int(self.width)

# print(Rectangle().area())


# 11
class Circle:
#     radius = int(input("Radius:  "))

    def area_circle(self):
        """returns the area of the circle """
        return round(math.pi * self.radius * self.radius, 2)

    def permeter_circle(self):
        """ returns the permeter of the circle """
        return round(2 * math.pi * self.radius, 2)


# print(Circle().area_circle())
# print(Circle().permeter_circle())
