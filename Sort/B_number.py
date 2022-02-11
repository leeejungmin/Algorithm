numbers = ['9', '5', '34', '3', '30']
numbers = list(map(str,numbers))
number=numbers.sort(key=lambda x:x*3,reverse=True)

print(numbers.sort(key=lambda x:x*3,reverse=True))
