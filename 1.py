
x = []
with open('i.txt','r') as f:
    x.append(f.readlines())
p = []

for y in x:
    for k in y:
        s=""
        for t in k:
            if t.isdigit():
                s+=t
        p.append(s)
print(sum([int(i[0] + i[-1]) for i in p]))

