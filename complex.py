# Diego 09/25/17
def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer,imagAnswer)
print complexAdd((1,2),(1,3))
print complexAdd((0,4),((22,-6)))
print complexAdd((0,4),complexAdd((22,-6),(15,-3)))

def complexSub(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer, imagAnswer)
print complexSub((5,7),(8,9))
print complexSub((0,9),(3,4))
print complexSub((0,9), complexSub((20,-2),(17,-3)))

def complexMul(a, b):
    realAnswer = a[1] * b[1]
    imagAnswer = a[0] * b[0]
    return (realAnswer, imagAnswer)
print complexMul((2, 8), (2, 1))
print complexMul((4, 2), (5, 1))
print complexMul((4, 2), complexMul((21,-4),(27,-9)))

def complexDiv(a, b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[0] / b[0]
    return (realAnswer, imagAnswer)
print complexDiv((2,5),(9,-1))
print complexDiv((7,5),(2,-2))
print complexDiv((7,5), complexDiv((24,-1),(15,-3)))








