
def hello():
    print('greetings user')

hello()


def pack(item1, item2, item3):
    return [item1, item2, item3]

print(pack('Jose ', 'is ', 'on a roll'))

def eat_food(thelist : list) -> str: #this function will return a string
    if len(thelist) == 1: #if there is only 1 element in the list
        return f'I only ate {thelist[0]}'
    elif len(thelist) != 0: #checks if length of list not 0 and that there are more than 1 elements
        myString = f'first I ate {thelist[0]}, '
        for i in range(len(thelist) - 1): #google says range() needs 1 arguement for stop
            myString += f'then I ate {thelist[i + 1]}, ' # plus 1 because we want to skip the first element.
        return myString
    else:
        return 'My lunchbox is empty!'

print(eat_food(['pizza']))
print(eat_food(['cereal', 'hamburger', 'salad']))