import json
import random
#获取json数据

def getjson(fileName=""):
    with open(fileName,mode='r',encoding="utf-8") as file:
        return json.loads(file.read())
data=getjson("data.json")
CelebrityQuotes = data["famous"] # a 代表前面垫话，b代表后面垫话
FrontWords = data["before"] # 在名人名言前面弄点废话
BackWords= data['after']  # 在名人名言后面弄点废话
nonsense= data['bosh'] # 代表文章主要废话来源
xx = "学生会退会"
Repeatability=2#重复度
def ShuffleTraversal(mylist):
    global Repeatability
    Pond = list(mylist) * Repeatability
    while True:
        random.shuffle(Pond)#打乱
        for element in Pond:
            yield element
#第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

nextnonsense = ShuffleTraversal(nonsense)
nextCelebrityQuotes = ShuffleTraversal(CelebrityQuotes)

def getCelebrityQuotes():
    global nextCelebrityQuotes#yield生成了一个生成器，next()可一直调用这个生成器
    xx = next(nextCelebrityQuotes)
    xx = xx.replace(  "a",random.choice(FrontWords) )
    xx = xx.replace(  "b",random.choice(BackWords) )
    return xx

def nextparagraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            Branch = random.randint(0,100)
            if Branch < 5:
                tmp += nextparagraph()
            elif Branch < 20 :
                tmp += getCelebrityQuotes()
            else:
                tmp += next(nextnonsense)
        tmp = tmp.replace("x",xx)#json数据中x代表题目事件
        print(tmp)