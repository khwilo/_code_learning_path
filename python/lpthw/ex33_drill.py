#i       = 0
numbers = []

def loop(num, increment):
    i = 0
    #while i < num:
    #    print "At the top i is %d" % i
    #    numbers.append(i)
    
    #    i += increment
    #    print "Numbers now: ", numbers
    #    print "At the bottom i is %d" % i

    for i in range(0, num):
        print "At the top i is %d" % i
        numbers.append(i)
        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
