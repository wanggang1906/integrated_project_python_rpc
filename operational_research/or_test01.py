# -*- coding: utf-8 -*-

# 运筹学求解器实战模块


import math
from scipy.optimize import linprog
import sys

def integerPro(c, A, b, Aeq, beq,t=1.0E-12):
    sys.setrecursionlimit(1000000) # 更改系统最大递归深度为1W次
    res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq)
    bestVal = sys.maxsize
    bestX = res.x
    if not(type(res.x) is float or res.status != 0):
        bestVal = sum([x*y for x,y in zip(c, bestX)])
    if all(((x-math.floor(x))<t or (math.ceil(x)-x)<t) for x in bestX):
        return (bestVal,bestX)
    else:
        ind = [i for i, x in enumerate(bestX) if (x-math.floor(x))>t and (math.ceil(x)-x)>t][0]
        newCon1 = [0]*len(A[0])
        newCon2 = [0]*len(A[0])
        newCon1[ind] = -1
        newCon2[ind] = 1
        newA1 = A.copy()
        newA2 = A.copy()
        newA1.append(newCon1)
        newA2.append(newCon2)
        newB1 = b.copy()
        newB2 = b.copy()
        newB1.append(-math.ceil(bestX[ind]))
        newB2.append(math.floor(bestX[ind]))
        r1 = integerPro(c, newA1, newB1, Aeq, beq)
        r2 = integerPro(c, newA2, newB2, Aeq, beq)
        if r1[0] < r2[0]:
            return r1
        else:
            return r2

if __name__ == '__main__':
    c = [3, 4, 1]
    A = [[-1, -6, -2], [-2, 0, 0]]
    b = [-5, -3]
    Aeq = [[0, 0, 0]]
    beq = [0]
    print(integerPro(c, A, b, Aeq, beq))