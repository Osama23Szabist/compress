from itertools import product
num = 1
def comboList(num):
    com = list(product([0, 1], repeat=num))
    return com

def clean_a_name(name):
    find = name.find("(")
    while find != -1:
        name = name[0:find] + name[find+1:len(name)]
        find = name.find("(")

    find = name.find(")")
    while find != -1:
        name = name[0:find] + name[find+1:len(name)]
        find = name.find(")")

    find = name.find(",")
    while find != -1:
        name = name[0:find] + name[find+1:len(name)]
        find = name.find(",")

    find = name.find(" ")
    while find != -1:
        name = name[0:find] + name[find+1:len(name)]
        find = name.find(" ")

    return name



com = []

listofchar = []

for i in range(0,(26)):
    listofchar.append(chr(97+i))
    listofchar.append(chr(65+i))

for i in range(0,10):
    listofchar.append(str(i))

#manual adding
listofchar.append("!")
listofchar.append("?")
listofchar.append("*")
listofchar.append(".")
listofchar.append("'")
listofchar.append("@")
listofchar.append("#")
listofchar.append("%")
listofchar.append("^")
listofchar.append("&")
listofchar.append(";")
listofchar.append(":")
listofchar.append("-")
listofchar.append("_")
listofchar.append("/")
listofchar.append("+")
listofchar.append("=")
listofchar.append("<")
listofchar.append(">")
listofchar.append("~")
listofchar.append("[")
listofchar.append("]")
listofchar.append("{")
listofchar.append("}")

listofchar.append("he")
listofchar.append("He")
listofchar.append("it")
listofchar.append("is")
listofchar.append("up")
listofchar.append("we")
listofchar.append("me")
listofchar.append("of")
listofchar.append("on")
listofchar.append("in")
listofchar.append("at")
listofchar.append("or")
listofchar.append("be")
listofchar.append("to")
listofchar.append("by")
listofchar.append("an")
listofchar.append("as")
listofchar.append("if")
listofchar.append("me")
listofchar.append("do")
listofchar.append("no")
listofchar.append("up")
listofchar.append("am")
listofchar.append("us")
listofchar.append("my")
listofchar.append("go")
listofchar.append("oh")
listofchar.append("hi")
listofchar.append("ok")
listofchar.append("ah")
listofchar.append("id")
listofchar.append("ex")
listofchar.append("um")
listofchar.append("yo")
listofchar.append("et")
listofchar.append("ad")

listofchar.append("i.e")
listofchar.append("she")
listofchar.append("She")
listofchar.append("why")
listofchar.append("how")
listofchar.append("now")
listofchar.append("man")
listofchar.append("and")
listofchar.append("but")
listofchar.append("the")
listofchar.append("for")
listofchar.append("not")
listofchar.append("you")
listofchar.append("all")
listofchar.append("are")
listofchar.append("can")
listofchar.append("was")
listofchar.append("one")
listofchar.append("our")
listofchar.append("out")
listofchar.append("use")
listofchar.append("who")
listofchar.append("get")
listofchar.append("new")
listofchar.append("let")
listofchar.append("had")
listofchar.append("his")
listofchar.append("its")
listofchar.append("day")
listofchar.append("any")
listofchar.append("may")
listofchar.append("say")
listofchar.append("too")
listofchar.append("off")
listofchar.append("per")
listofchar.append("end")
listofchar.append("set")
listofchar.append("run")
listofchar.append("own")
listofchar.append("own")
listofchar.append("old")
listofchar.append("two")
listofchar.append("way")
listofchar.append("see")
listofchar.append("yes")
listofchar.append("top")
listofchar.append("bad")
listofchar.append("big")
listofchar.append("red")
listofchar.append("boy")
listofchar.append("put")
listofchar.append("job")
listofchar.append("few")
listofchar.append("yet")
listofchar.append("lie")
listofchar.append("key")
listofchar.append("try")
listofchar.append("low")

listofchar.append("this")
listofchar.append("here")
listofchar.append("king")
listofchar.append("name")
listofchar.append("bear")
listofchar.append("kind")
listofchar.append("that")
listofchar.append("with")
listofchar.append("will")
listofchar.append("have")
listofchar.append("been")
listofchar.append("just")
listofchar.append("more")
listofchar.append("only")
listofchar.append("than")
listofchar.append("from")
listofchar.append("some")
listofchar.append("into")
listofchar.append("time")
listofchar.append("down")
listofchar.append("made")
listofchar.append("tell")
listofchar.append("love")
listofchar.append("know")
listofchar.append("live")
listofchar.append("much")
listofchar.append("hard")
listofchar.append("good")
listofchar.append("help")
listofchar.append("come")
listofchar.append("back")
listofchar.append("look")
listofchar.append("find")
listofchar.append("side")
listofchar.append("want")
listofchar.append("give")
listofchar.append("take")
listofchar.append("also")
listofchar.append("long")
listofchar.append("must")
listofchar.append("call")
listofchar.append("play")
listofchar.append("stop")
listofchar.append("work")
listofchar.append("part")
listofchar.append("deal")
listofchar.append("year")
listofchar.append("into")
listofchar.append("real")
listofchar.append("move")
listofchar.append("idea")
listofchar.append("step")
listofchar.append("wish")
listofchar.append("away")
listofchar.append("show")
listofchar.append("unit")
listofchar.append("sand")

listofchar.append("there")
listofchar.append("their")
listofchar.append("hello")
listofchar.append("world")
listofchar.append("story")
listofchar.append("large")
listofchar.append("house")
listofchar.append("group")
listofchar.append("water")
listofchar.append("apple")
listofchar.append("peace")
listofchar.append("laugh")
listofchar.append("money")
listofchar.append("light")
listofchar.append("right")
listofchar.append("smile")
listofchar.append("dance")
listofchar.append("music")
listofchar.append("grape")
listofchar.append("train")
listofchar.append("mount")
listofchar.append("dream")
listofchar.append("black")
listofchar.append("white")
listofchar.append("heart")
listofchar.append("table")
listofchar.append("grass")
listofchar.append("sugar")
listofchar.append("chose")
listofchar.append("march")
listofchar.append("strom")
listofchar.append("night")
listofchar.append("stone")
listofchar.append("plane")
listofchar.append("sleep")
listofchar.append("watch")
listofchar.append("paint")
listofchar.append("drink")
listofchar.append("angle")
listofchar.append("quick")
listofchar.append("touch")
listofchar.append("brown")
listofchar.append("shelf")
listofchar.append("sight")
listofchar.append("candy")
listofchar.append("laugh")
listofchar.append("begin")
listofchar.append("glove")
listofchar.append("fruit")
listofchar.append("clean")
listofchar.append("style")
listofchar.append("about")
listofchar.append("above")
listofchar.append("after")
listofchar.append("again")
listofchar.append("agree")
listofchar.append("alarm")
listofchar.append("alien")
listofchar.append("amaze")
listofchar.append("anger")
listofchar.append("apple")
listofchar.append("apply")
listofchar.append("audio")
listofchar.append("award")
listofchar.append("aware")
listofchar.append("beauty")
listofchar.append("begin")
listofchar.append("below")
listofchar.append("bench")
listofchar.append("bills")
listofchar.append("bored")
listofchar.append("brave")
listofchar.append("bread")
listofchar.append("build")
listofchar.append("busy")
listofchar.append("candy")
listofchar.append("cause")
listofchar.append("chain")
listofchar.append("chart")
listofchar.append("chase")
listofchar.append("cheap")
listofchar.append("cheer")
listofchar.append("child")
listofchar.append("class")
listofchar.append("clean")
listofchar.append("clear")
listofchar.append("close")
listofchar.append("cloud")
listofchar.append("coach")
listofchar.append("color")
listofchar.append("coming")
listofchar.append("complete")
listofchar.append("cover")
listofchar.append("cycle")
listofchar.append("dance")
listofchar.append("death")
listofchar.append("decide")
listofchar.append("delight")
listofchar.append("doing")
listofchar.append("early")
listofchar.append("earth")
listofchar.append("email")
listofchar.append("empty")
listofchar.append("enter")
listofchar.append("equal")
listofchar.append("error")
listofchar.append("event")
listofchar.append("exact")
listofchar.append("extra")
listofchar.append("false")
listofchar.append("favor")
listofchar.append("first")
listofchar.append("focus")
listofchar.append("force")
listofchar.append("front")
listofchar.append("funny")
listofchar.append("grade")
listofchar.append("grape")
listofchar.append("green")
listofchar.append("group")
listofchar.append("happy")
listofchar.append("heart")
listofchar.append("heavy")
listofchar.append("helpful")
listofchar.append("honor")
listofchar.append("house")
listofchar.append("hover")
listofchar.append("human")
listofchar.append("image")
listofchar.append("imagine")
listofchar.append("inner")
listofchar.append("input")
listofchar.append("issue")
listofchar.append("jolly")
listofchar.append("judge")
listofchar.append("jump")
listofchar.append("jumpy")
listofchar.append("joint")
listofchar.append("jolly")
listofchar.append("keep")
listofchar.append("key")
listofchar.append("laugh")
listofchar.append("large")
listofchar.append("laser")
listofchar.append("leafy")
listofchar.append("lemon")
listofchar.append("level")
listofchar.append("light")
listofchar.append("lucky")
listofchar.append("lunar")
listofchar.append("major")
listofchar.append("march")
listofchar.append("medal")
listofchar.append("money")
listofchar.append("music")
listofchar.append("north")
listofchar.append("noble")
listofchar.append("night")
listofchar.append("noise")
listofchar.append("occur")
listofchar.append("offer")
listofchar.append("order")
listofchar.append("other")
listofchar.append("paint")
listofchar.append("party")
listofchar.append("place")
listofchar.append("plant")
listofchar.append("play")
listofchar.append("power")
listofchar.append("pride")
listofchar.append("prime")
listofchar.append("queen")
listofchar.append("quick")
listofchar.append("quiet")
listofchar.append("ready")
listofchar.append("right")
listofchar.append("round")
listofchar.append("rose")
listofchar.append("score")
listofchar.append("serve")
listofchar.append("shape")
listofchar.append("show")
listofchar.append("silly")
listofchar.append("smart")
listofchar.append("space")
listofchar.append("start")
listofchar.append("store")
listofchar.append("study")
listofchar.append("style")
listofchar.append("super")
listofchar.append("sweet")
listofchar.append("taken")
listofchar.append("teach")
listofchar.append("thank")
listofchar.append("think")
listofchar.append("throw")
listofchar.append("tight")
listofchar.append("total")
listofchar.append("truth")
listofchar.append("under")
listofchar.append("unity")
listofchar.append("value")
listofchar.append("vapor")
listofchar.append("video")
listofchar.append("visit")
listofchar.append("voice")
listofchar.append("vote")
listofchar.append("watch")
listofchar.append("water")
listofchar.append("where")
listofchar.append("woman")
listofchar.append("world")
listofchar.append("young")
listofchar.append("youth")
listofchar.append("your")
listofchar.append("zebra")
listofchar.append("zero")
listofchar.append("zesty")
listofchar.append("abuse")
listofchar.append("adore")
listofchar.append("alert")
listofchar.append("allow")
listofchar.append("anger")
listofchar.append("askew")
listofchar.append("bless")
listofchar.append("burn")
listofchar.append("beach")
listofchar.append("caste")
listofchar.append("cost")
listofchar.append("climb")
listofchar.append("candy")
listofchar.append("chirp")
listofchar.append("dash")
listofchar.append("edge")
listofchar.append("farce")
listofchar.append("feast")
listofchar.append("field")
listofchar.append("flask")
listofchar.append("flood")
listofchar.append("fame")
listofchar.append("flock")
listofchar.append("fold")
listofchar.append("gape")
listofchar.append("grip")
listofchar.append("gush")
listofchar.append("gnaw")
listofchar.append("hope")
listofchar.append("hair")
listofchar.append("hint")
listofchar.append("hunt")
listofchar.append("herd")
listofchar.append("house")
listofchar.append("hatch")
listofchar.append("helic")
listofchar.append("later")
listofchar.append("level")
listofchar.append("march")
listofchar.append("maker")
listofchar.append("mate")
listofchar.append("match")
listofchar.append("meant")
listofchar.append("merry")
listofchar.append("model")
listofchar.append("mount")
listofchar.append("mouth")
listofchar.append("name")
listofchar.append("note")
listofchar.append("paste")
listofchar.append("paid")
listofchar.append("pleasure")
listofchar.append("plan")
listofchar.append("szabist")
listofchar.append("school")
listofchar.append("university")
listofchar.append("Osama")
listofchar.append("Ali")
listofchar.append("programming")
listofchar.append("The")

hold = []

with open("osama.txt","r",encoding='utf-8') as file:
    while True:
        line = file.readline().strip()
        if line:
            hold.append(line)
        else:
            break
    
for i in range(0,len(hold)):
    listofchar.append(hold[i])

for i in range(0,len(listofchar)):
    min = i
    for j in range(i,len(listofchar)):
        if len(listofchar[min]) > len(listofchar[j]):
            min = j

    if min != i:
        temp = listofchar[i]
        listofchar[i] = listofchar[min]
        listofchar[min] = temp

com = comboList(num)
for i in range(0,len(listofchar)):
    if len(com) == 0:
        num +=1
        com = comboList(num)
    listofchar[i] = listofchar[i] + "*0" + clean_a_name(str(com[len(com)-1]))
    com.remove((com[len(com)-1]))


with open("list.txt","w",encoding='utf-8') as file:
    for data in listofchar:
        file.write(data)
        file.write("\n")


print("remaining",len(com),"size",len(com[0]),"bit and +1 ")
