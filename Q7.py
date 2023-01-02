from statistics import mean

def seq(terms):
    if terms <= 0: raise ValueError("Please enter a postive no. of terms")
    elif terms == 1 : return [0]
    elif terms == 2 : return [0,1]
    else:
        seq = [0,1]
        num = 2
        while(num < terms) :
            seq.append(seq[num - 1] + seq[num - 2])
            num += 1
        return seq

fibo = seq(int(input("Enter no. of terms in sequence : ")))
print(fibo)

print(round(mean(fibo),2))