from math import exp
def logistic(value):
    return 1/(1+exp(-value))

b1 = 0
b2 = 0
w1 = -6.90675478
w2 = 0.40546511
h1 = 0
h2 = 1
v = 1
h11 = logistic(-b1)
h21 = logistic(-b2)
v1 = logistic(w1*(h1) + w2*h2)

def point1(h1,h2,weight1=w1,weight2=w2):
    return logistic(weight1*h1 + weight2*h2)

def point2():

    for i in [0,1]:
        for j in [0,1]:
            v = point1(i,j)/4
            print("point 2 h1 = %s h2 = %s v = [%s, %s]" % (i,j,1/4-v,v))

    return

def point34():
    print('point3 ', 0)
    print('point 4', exp(-w2)/(1+exp(-w2)))

def point5():
    upper = point1(0,1,10,-4)*0.5
    down = upper + point1(0,0,10,-4)*0.5
    print('point5 ', upper/down)

def point6():
    upper = point1(1, 1, 10, -4) * 0.5
    down = upper + point1(1,0,10,-4)*0.5
    print('point6 ', upper/down)

print('probs for h1 = %s and h2 = %s' % (h11, h21))
print('probs for v1 = %s' % v1)
print('prob for h1,h2 = 0,0', point1(0,0))
point2()
point34()
point5()
point6()

