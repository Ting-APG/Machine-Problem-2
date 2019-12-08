from math import*
def ThreePoints(x1,y1,x2,y2,x3,y3):   
    A1 = x1*(y2-y3)
    A2 = (y1*(x2-x3))
    A3 = x2*y3
    A4 = x3*y2
    A = A1 - A2 + A3 - A4
    'Value for A'
    D1 = (x1**2+y1**2)*(y3-y2)
    D2 = (x2**2 + y2**2)*(y1-y3)
    D3 = (x3**2+y3**2)*(y2-y1)
    D = D1 + D2+ D3
    'Values for B'
    E1 = (x1**2+y1**2)*(x2-x3)
    E2 = (x2**2 + y2**2)*(x3-x1)
    E3 = (x3**2+y3**2)*(x1-x2)
    E = E1 + E2 + E3
    'Values for C'
    F1 = (x1**2+y1**2)*((x3*y2)-(x2*y3))
    F2 = (x2**2 + y2**2)*((x1*y3)-(x3*y1))
    F3 = (x3**2+y3**2)*((x2*y1)-(x1*y2))
    F = F1 + F2 + F3
    'Values for D'
    X = -D/(2*A)
    Y = -E/(2*A)
    R = sqrt(((D**2)+(E**2)-4*(A*F))/(4*A**2))
    H = D/(2*A)
    K = E/(2*A)
    Dequation = D/A
    Eequation = E/A
    Fequation = F/A
    print("center is ",H,K)
    print('The radiues is ', R)
    print('The Vector D,E,F'Dequation,Eequation,Fequation)