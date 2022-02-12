import hashlib

a='032fba424a63c15c898039239f13387d6bcf828e'

for i in range(10000000,99999999+1):
    pw = (str(i) + "salt_for_you")
    for j in range(500):
        pw = hashlib.sha1(pw.encode()).hexdigest()
    print('process' + str(i))
    if(pw == a):
        print('Find Flag : ' + str(i)+"salt_for_you")
        break
    
