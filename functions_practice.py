
# hello function
def hello():
    print("Hola Mundo!!!")
    
hello()

# pack function

def pack(width, height, length):
    pack = width, height, length
    print(list(pack))
    
    
pack(1, 2, 3)

# eat lunch function


food = ["bread", "fish", "apple", "chicken", "beef"]
empty = []

def eat_lunch(list):
    
    if list == [] :
        print("My lunch box is empty")
        
    else:
        for e in list:
            print(f"I eat {e}")
        
eat_lunch(empty)