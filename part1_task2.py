#square_number=int(input('Input number: '))
#test_square_number=square_number**2
#print('Answer is: ',test_square_number)

def square_number(test):
    return test**2
def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
print("YOUR CODE IS CORRECT!")
test_square_number()












