#// PYTHON
#      >>> def r(pwd, fr, to, by):
#      ...     return ''.join([pwd[i] for i in range(fr, to, by)])
#Output:
#>>> print(r(pwd, 0, 4, 1))
#42f3
#>>> print(r(pwd, 4, 20, 2))
#a2cd3c05
#>>> print(r(pwd, 5, 30, 3))
#fc4c5ba15
#>>> print(r(pwd, 5, 40, 4))
#fab55c599
#>>> print(r(pwd, 6, 40, 6))
#235426
#>>> print(r(pwd, 7, 8, 1))
#5
#>>> print(r(pwd, 10, 40, 3))
#db048cfee9
#>>> print(r(pwd, 10, 40, 5))
#d1bc2f
#>>> print(r(pwd, 15, 40, 6))
#15893
#>>> print(r(pwd, 20, 40, 3))
#ba156f2

#Given a function r that requires a password, a from index, a to index, and a step value,
#the function returns a substring of the password starting from the 'from' index to the 'to' index,
#The goal is to extract specific parts of the password based on the indices and step values provided.

#START WITH THE CODE
#global PWD CHAR ARRAY

pwd = [''] * 40

def inverse_r(output_str, fr, to, by):
    for idx, i in enumerate(range(fr, to, by)):
        pwd[i] = output_str[idx]

def step1():
    inverse_r("42f3", 0, 4, 1)

def step2():
    inverse_r("a2cd3c05", 4, 20, 2)

def step3():
    inverse_r("fc4c5ba15", 5, 30, 3)

def step4():
    inverse_r("fab55c599", 5, 40, 4)

def step5():
    inverse_r("235426", 6, 40, 6)

def step6():
    inverse_r("5", 7, 8, 1)

def step7():
    inverse_r("db048cfee9", 10, 40, 3)

def step8():
    inverse_r("d1bc2f", 10, 40, 5)

def step9():
    inverse_r("15893", 15, 40, 6)

def step10():
    inverse_r("ba156f2", 20, 40, 3)

if __name__ == "__main__":
    # NO borrar ni modificar pwd aquí
    step1()
    step2()
    step3()
    step4()
    step5()
    step6()
    step7()
    step8()
    step9()
    step10()
    
    print(f"🔐 Password: {''.join(pwd)}")
