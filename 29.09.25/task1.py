def greet(name):
    print(f"привет, {name}!")
greet("Леша")

def square(number):
    return number**2
print(square(4))


def max_of_two(x, y):
    if x>y:              
        return x            
    else:          
        return y
    
print(max_of_two(322, 666))