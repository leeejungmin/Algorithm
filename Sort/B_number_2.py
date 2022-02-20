numbers = ['9', '5', '34', '3', '30']
numbers.sort(key = lambda x:x*3,reverse=True )
numbers=str(int(''.join(numbers)))
print(numbers)
