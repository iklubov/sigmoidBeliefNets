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

def point1(h1,h2):
    return logistic(w1*h1 + w2*h2)

def point2():
    for i in [0,1]:
        for j in [0,1]:
            v = point1(i,j)
            print("point 2 i = %s j = %s v = %s" % (i,j,v))
    return
print('probs for h1 = %s and h2 = %s' % (h11, h21))
print('probs for v1 = %s' % v1)
point2()

