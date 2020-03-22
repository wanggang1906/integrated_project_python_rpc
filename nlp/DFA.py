#coding:UTF-8
# DFA有限状态自动机
a = input('输入羊叫: ')
a = list(a)
b = [[1,0,0],[0,2,0],[0,3,0],[0,3,4],[0,0,0]]
def deterministic(tape,machine):
    j=0
    reject='接受'
    accept='拒识'
    for i in range(len(tape)):
        if tape[i]=='b':
            if machine[j][0]==0:
                break
            else:
                j=machine[j][0]
                if tape[i]=='a':
                    if machine[j][1]==0:
                        break
                    else:
                        j=machine[j][1]
                        if tape[i]=='!':
                            if machine[j][2]==0:
                                break
                            else:
                                j=machine[j][2]
    if j==4:
        return accept
    else:
        return reject

print(deterministic(a,b))
