import math 
def NPA (indexes:list):
    """
    This function calculates the NPA (Nivel de Presión Acústica) based on the given parameters.
    """
    NPA = 10 * math.log10(sum(10**(i/10) for i in indexes))
    
    return NPA

solution = NPA([51.8, 64.9, 66.4, 75.8, 81, 83.2, 80, 68.9])
print("NPAi:", solution)

solution2 = NPA([48.8, 62.9, 64.4, 70.8, 75, 76.2, 74, 62.9])
print("NPAi 2:", solution2)

solution3 = NPA([72.2, 80.8, 75, 79, 81, 81.8, 78.2, 67])
print("NPAi 3:", solution3)

solution4 = NPA([93.36,92.91, 93.42])
print("NPAi 4:", solution4)

solution5 = NPA([87.34, 86.98])
print("NPAi 5:", solution5)

solution6 = NPA([93.98, 86.53])
print("NPAi 6:", solution6)

solution7 = NPA([91.35, 92.43, 87])
print("NPAi 7:", solution7)

def LAEQD (inputL,inputT):
    """
    This function calculates the L_aeqd based on the given parameters.
    """
    # inputT is the time
    # inputL is a value
    Laeqd = inputL + 10 * math.log10(inputT/480)
    
    return Laeqd

print("======================================")

solution8 = LAEQD(96.19, 250)
print("L_aeqd 1:", solution8)

solution9 = LAEQD(97.17, 180)
print("L_aeqd 2:", solution9)

solution10 = LAEQD(99.03, 132)
print("L_aeqd 3:", solution10)

solution11 = LAEQD(96.11, 480)
print("L_aeqd 4:", solution11)

solution12 = LAEQD(99.82, 125)
print("L_aeqd 5:", solution12)

solution13 = LAEQD(97.23, 124)
print("L_aeqd 6:", solution13)

solution14 = LAEQD(90.78, 201)
print("L_aeqd 7:", solution14)
