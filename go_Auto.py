from flask import Flask, render_template, request
import random
import json
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/Auto_index', methods=['GET', 'POST'])
def Auto_index():
    return render_template('Auto_index.html')
@app.route('/Auto_add',methods=['GET','POST'])
def Auto_add():
    id = request.form['id']
    print(id)
    if id == 'bei':
        question = request.form['q']
        answer=getanswer(question)
        # print(answer)
        return answer
    else:
        pass


def getanswer(question):
    data = getjson("data.json")
    CelebrityQuotes = data["famous"]  # a 代表前面垫话，b代表后面垫话
    FrontWords = data["before"]  # 在名人名言前面弄点废话
    BackWords = data['after']  # 在名人名言后面弄点废话
    nonsense = data['bosh']  # 代表文章主要废话来源
    nextnonsense = ShuffleTraversal(nonsense)
    # nextCelebrityQuotes = ShuffleTraversal(CelebrityQuotes)
    answer=str()
    for x in question:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            Branch = random.randint(0,100)
            if Branch < 5:
                tmp += nextparagraph()
            elif Branch < 20 :
                tmp += getCelebrityQuotes(CelebrityQuotes,FrontWords,BackWords)
            else:
                tmp += next(nextnonsense)
        tmp = tmp.replace("x",question)#json数据中x代表题目事件
        answer += tmp
    return answer

#---------------处理自动生成文章代码
def getjson(fileName=""):
    with open(fileName,mode='r',encoding="utf-8") as file:
        return json.loads(file.read())
def ShuffleTraversal(mylist):
    Repeatability=2
    Pond = list(mylist) * Repeatability
    while True:
        random.shuffle(Pond)#打乱
        for element in Pond:
            yield element
def getCelebrityQuotes(CelebrityQuotes,FrontWords,BackWords):
    nextCelebrityQuotes = ShuffleTraversal(CelebrityQuotes)#yield生成了一个生成器，next()可一直调用这个生成器
    xx = next(nextCelebrityQuotes)
    xx = xx.replace(  "a",random.choice(FrontWords) )
    xx = xx.replace(  "b",random.choice(BackWords) )
    return xx
def nextparagraph():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == '__main__':
    app.debug=True
    app.run()