# import spacy
# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
def main():
    # nlp = en_core_web_sm.load()
    # doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
    # pprint([(X.text, X.label_) for X in doc.ents])
    # l = ["aAaA", "nbbb", "B"]
    # l = [i.lower() for i in l ]
    # # f = []
    # # f[0].append(list["AA"])
    # # f[1].append(["BB"])
    # d = [[] for x in range(3)]
    # d[0] = ["ehye"]
    # d[0].append("aaa")
    # d[1] = ["lsjl"]
    # print(d)
    # # l.sort(key=str.casefold)
    # for i, c in enumerate(l,start=2):
    #     print(i)
    # # print(l)
    # l = []
    # l.append("mount")
    # l.append("mountain")
    # l.append("mousepad")
    # l.append("mouse")
    # l.append("moose")
    # swamz(5, l, "mouse")]
    l = [[0,0,1,0,1],
         [1,0,1,0,1],
         [1,0,1,0,1],
         [1,0,1,0,1],
         [1,0,1,0,1]]
    amz2(l)
    return

def amz2(l):
    p1= 0
    p3 = 0
    j = 0
    k = 0
    for col in l[j]:
        print(col)
        for row in range(l[j][k]):
            print(f'row: {row}')
            pass
    j+=1



def swamz(sizerepo, repo: list, sugg):
    repo.sort()
    # print(repo)
    count = 0
    listindex = 0
    sugglist = [[] for x in range(1,sizerepo)]
    for isug in range(2, len(sugg)):
        for word in repo:
            if len(sugglist[listindex]) < 3 and word[isug] == sugg[isug]:
                if word[:isug] == sugg[:isug]:
                    sugglist[listindex].append(word)
        listindex+=1
    sugglist = [i for i in sugglist if i]
    print(*sugglist)


    








def countprimes(n:int) -> int:
    count = 0

    if n > 1:
        for i in range(2, n//2):
            count +=1
            if n % i == 0:
                return 0
        return count
    else:
        return 0
def fizzbizz(n: int) -> list:
    l = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(i))
    return l
        

def amazondemo():
    p1 = 0
    p3 = 2
    l = [1,0,1,0,1]
    d = {}
    days = 3
    for index, val in enumerate(l):
        d[i] = [val, 0]
    for day in range(days):
        for i in range(p1+1, len(l) -1):
            if l[p1] == l[p3]:
                d[i] = [0, day+1]
            else:
                l[i] = 1
            p1+=1
            p3+=1
        
    print(l)



def findcommongcb(l: list):
    l = [4,8,10,14]
    a = l[0]
    for i in l[1:]:
        a = gcd(a, i)
    print(a)
    return a

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a




if __name__ == "__main__":
    main()