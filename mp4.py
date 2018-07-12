import math

cosmos = "0123456789ABCDEFGHJKMNPQRSTVWXYZ" 
legend = []
for x in cosmos:
    legend.append(x)

def PutBaseConversion(quo,b):
    #quo = n // b
    #rem = n % b
    if (b == 1):
        return "?"
    current = legend[0:b]
    #for x in current:
    #    print(x, end=' ')
    temp = []
    #print(quo, end = ' ')
    #print(b,end=' ')
    while True:
        rem = quo % b
        quo = quo // b
        #print("quo= ", quo, " rem= ", rem)  
        temp.append(current[rem])
        if (quo == 0):
            break
    #for x in temp:
        #print (x,end = ' ')
    str1 = ''.join(temp)
    temp = []
    #print("test str1\n", ' ')
    #print(str1)
    str2 = str1[::-1]
    return str2

def main():

    buf = []
    a = 1
    b = 0
    buf.append(b)
    for i in range(0,32):
        c = a + b
        buf.append(a)
        b = a 
        a = c
    buf.append(a)
    for i in range(0,32):
        #print buf[i]
        j = i + 1
        fuck = buf[i]
        print(PutBaseConversion(fuck,j))

    #for i in range(0,32):
    #    print(PutBaseConversion(buf[i],i+1))

    
if __name__ == "__main__":
    main()
print("\nfinish")
