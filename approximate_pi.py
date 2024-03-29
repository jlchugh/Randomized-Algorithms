import random
def dist(x, y):
    return (x*x + y*y)**.5

#n = int(input("enter number of samples: "))
n = 100000
def calc_pi(n):

    pairs = []
    for i in range(0, n):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        pairs.append([x,y])

    in_circle_count = 0

    for pair in pairs:
        #print("pair = " +str(pair))
        if dist(pair[0], pair[1]) <= 1:
            in_circle_count += 1

    # we must mutiply 4 becuase we are calculating pi/4
    # we calculate pi by calculating the ratio of a circle with radius 1 inside of a square
    # pi r r / 4 r r = pi/4
    return (4 * in_circle_count/float(n))

sum = 0
for i in range(10000):
    sum += calc_pi(10000)
sum = sum/10000
print("pi = " + str(sum))
