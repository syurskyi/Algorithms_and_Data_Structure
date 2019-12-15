def reverseWordOrder(forward):
    substrings = forward.split()

    return ' '.join(reversed(substrings))

userinput = input("Enter a string: ")

print(reverseWordOrder(userinput))

'''
Shorter and more efficient solution, from user comments:

def reverseWordOrder(forward):
  return ' '.join(forward.split()[::-1])

userinput = input("Enter a string: ")

print(reverseWordOrder(userinput))

'''
