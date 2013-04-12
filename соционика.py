import re

working=True
while(working):
    class Tip:
        def __init__(self, e=0, s=0, i=0, r=0):
            self.sensoric = s
            self.etic = e
            self.racional = r
            self.introvert = i
        def opr(self):
            if self.sensoric<4 and self.etic<4 and self.racional<4 and self.introvert<4:
                return("дон кихот")
            elif self.sensoric>=4 and self.etic>=4 and self.racional<4 and self.introvert>=4:
                return("дюма")
            elif self.sensoric>=4 and self.etic>=4 and self.racional>=4 and self.introvert<4:
                return("гюго")
            elif self.sensoric<4 and self.etic<4 and self.racional>=4 and self.introvert>=4:
                return("робеспьер")
            elif self.sensoric<4 and self.etic>4 and self.racional>=4 and self.introvert<4:
                return("гамлет")
            elif self.sensoric>=4 and self.etic<4 and self.racional>=4 and self.introvert>=4:
                return("горький")                
            elif self.sensoric>=4 and self.etic<4 and self.racional<4 and self.introvert<4:
                return("жуков")
            elif self.sensoric<4 and self.etic>=4 and self.racional<4 and self.introvert>=4:
                return("есенин")
            elif self.sensoric>=4 and self.etic>=4 and self.racional<4 and self.introvert<4:
                return("наполеон")
            elif self.sensoric<4 and self.etic<4 and self.racional<4 and self.introvert>=4:
                return("бальзак")
            elif self.sensoric<4 and self.etic<4 and self.racional>=4 and self.introvert<4:
                return("джек лондон")
            elif self.sensoric>=4 and self.etic>=4 and self.racional>=4 and self.introvert>=4:
                return("драйзер")
            elif self.sensoric>=4 and self.etic<4 and self.racional>=4 and self.introvert<4:
                return("штирлиц")
            elif self.sensoric<4 and self.etic>=4 and self.racional>=4 and self.introvert>=4:
                return("достоевский")
            elif self.sensoric<4 and self.etic>=4 and self.racional<4 and self.introvert<4:
                return("гексли")
            elif self.sensoric>=4 and self.etic<4 and self.racional<4 and self.introvert>=4:
                return("габен")
    you=Tip()
    i=0
    with open('intro.txt') as base:
        intro=base.readlines()
    while(i<7):
        print(intro[i])
        l=input("нажмите L если вам подходит левое слово или R если вам подходит правое:\n")
        l=l.lower()
        i+=1
        if l=='r':
            you.introvert+=1
        elif l=='l':
            pass
        else:
            print("Вы ввели неверное значение, попробуйте ответить на этот вопрос снова:\n")
            i-=1
    i=0
    with open('sencoric.txt') as base:
        sencoric=base.readlines()
    while(i<7):
        print(sencoric[i])
        l=input("нажмите L если вам подходит левое слово или R если вам подходит правое:\n")
        i=i+1
        l=l.lower()
        if l=='l':
            you.sensoric+=1
        elif l=='r':
            pass
        else:
            print("Вы ввели неверное значение, попробуйте ответить на этот вопрос снова:\n")
            i-=1
    i=0
    with open('logic.txt') as base:
        logic=base.readlines()
    while(i<7):
        print(logic[i])
        l=input("нажмите L если вам подходит левое слово или R если вам подходит правое:\n")
        i+=1
        l=l.lower()
        if l=='r':
            you.etic+=1
        elif l=='l':
            pass
        else:
            print("Вы ввели неверное значение, попробуйте ответить на этот вопрос снова\n")
            i-=1
    i=0
    with open('racio.txt') as base:
        racio=base.readlines()
    while(i<7):
        print(racio[i])
        l=input("нажмите L если вам подходит левое слово или R если вам подходит правое:\n")
        i=i+1
        l=l.lower()
        if l=='l':
            you.racional+=1
        elif l=='r':
            pass
        else:
            print("Вы ввели неверное значение, попробуйте ответить на этот вопрос снова\n")
            i-=1
    print("Вы - "+you.opr())
    p=input("Вы получили рзультат, хотите ли вы продолжить?(да/нет):\n")
    if p not in ("yes", "Y", "да", "Да"):
        working=False
    

