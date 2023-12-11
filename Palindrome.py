
# Online Python - IDE, Editor, Compiler, Interpreter

def palindrome(word):
    word = word.lower()
    list_string = []
    forward = ""
    backward = ""
    list_string = word.split()
    #for i in range(len(word)):
    #    list_string.append(i)
    #print(list_string)
    for i in list_string:
        rightward = rightward + list_string[i]
    for i in list_string:
        backward = list_string[i] + backward
    if backward == forward:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    

palindrome("Okay")
    
    #return rightward, backward

#a = int(input('Enter 1st number: '))
#b = int(input('Enter 2nd number: '))

#print(f'Sum of {a} and {b} is {sum(a, b)}')
