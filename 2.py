x = "one2131wad23two231"

t = [["one",1], ["two",2], ["three",3], ["four",4], ["five",5], ["six",6], ["seven",7], ["eight",8], ["nine",9]]

p = open('i.txt','r').readlines()

k=[]

def find_all_occurrences(string, substring):
    occurrences = []
    index = string.find(substring)

    while index != -1:
        occurrences.append(index)
        index = string.find(substring, index + 1)

    return occurrences

for i in p:
    a = []
    for search in t:
        awdawd = find_all_occurrences(i,search[0])
        for pepe in awdawd:
            a.append([pepe,search[1]])
    for j in range(0,len(i)):
        if i[j].isdigit():
            a.append([j,i[j]])
    k.append(a)
            
s = 0
for pp in k:
    n = sorted(pp, key=lambda x: x[0])
    print(int(str(n[0][1]) + str(n[-1][1])),n)
    s+=int(str(n[0][1]) + str(n[-1][1]))
    
print(s)