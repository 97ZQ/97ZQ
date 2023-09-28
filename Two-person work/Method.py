import random
from fractions import Fraction
import os
#将列表的分数变成真分数
def standardFraction(list,allOperators):
    listNew=[]
    for item in list:
        if type(item) == Fraction:
            a = item
            #分母不等于一，分子大于分母的
            if a.denominator != 1 and a.numerator > a.denominator:

                itemNew = str(a.numerator // a.denominator) + "'" + str(
                    a - a.numerator // a.denominator)
                listNew.append(itemNew)
            else:
                listNew.append(item)
        else:
            listNew.append(item)
    return listNew
#生成随机数，注意不要让分母太大
def genarateNumber(r):
    choice = random.randint(0,1)
    if choice ==0:
        upNumber = random.randint(0,r*r)
        downNumber = random.randint(1,r)
        number = Fraction(upNumber ,downNumber).limit_denominator()
    else :
        number =  random.randint(0,r)
    if number<0 or number > r:
        return genarateNumber(r)
    else:
        return number
#生成一个括号的情况
def OneBrackets(list,first,second):
    listNew = []
    for i in range(len(list)):
        if i == first:
            listNew.append('(')
            listNew.append(list[i])
        elif i == second:
            listNew.append(list[i])
            listNew.append(')')
        else:
            listNew.append(list[i])
    return listNew
#生成两个括号的情况
def TwoBrackets(list,first,second,third,forth):
    listNew = []
    for i in range(len(list)):
        if i == first or i == second or i == third or i == forth:
            if i == first :
                listNew.append('(')
            if i ==third :
                listNew.append('(')
            listNew.append(list[i])
            if i == second:

                listNew.append(')')
            if i == forth:

                listNew.append(')')
        else:
            listNew.append(list[i])
    return listNew
#标准化表达式，为算术表达式中的每一项之间都添加空格
def addBlank(list):
    s = ""
    for i in range(len(list)):
        if i == len(list) - 1:
            s += str(list[i])
        else:
            s += str(list[i]) + ' '
    return s
#为算数表达式生成括号的方法
def addBracket(operatorNum,list):
    #如果是只有一个算数符如：1 + 1就不需要括号，就不用该表该列表
    if operatorNum == 1:
        return list
    #当两个运算符的时候，通过枚举法列出可能存在括号的情况，然后随机选择括号的位置
    if operatorNum == 2:
        choice = random.randint(0,2)
        if choice ==0:
            return list
        elif choice == 1:
            listNew = OneBrackets(list,0,2)
            return listNew
        elif choice == 2:
            listNew = OneBrackets(list,2,4)
            return listNew
        # 当三个运算符的时候，通过枚举法列出可能存在括号的情况，然后随机选择括号的位置
    if operatorNum ==3:
        choice = random.randint(0,10)
        if choice == 0:
            return list
        elif choice == 1:
            listNew = OneBrackets(list, 0, 2)
            return listNew
        elif choice ==2:
            listNew = OneBrackets(list,2,4)
            return listNew
        elif choice ==3:
            listNew = OneBrackets(list,4,6)
            return listNew
        elif choice == 4:
            listNew = OneBrackets(list,0,4)
            return listNew
        elif choice ==5:
            listNew = OneBrackets(list,2,6)
            return listNew
        elif choice == 6:
            listNew=TwoBrackets(list,0,2,0,4)
            return listNew
        elif choice ==7:
            listNew =TwoBrackets(list,0,4,2,4)
            return listNew
        elif choice == 8:
            listNew = TwoBrackets(list,2,6,2,4)
            return listNew
        elif choice ==9 :
            listNew = TwoBrackets(list,2,6,4,6)
            return listNew

        elif choice == 10:
            listNew = TwoBrackets(list,0,2,4,6)
            return listNew
def generateQuestionAndAnswer(r,n):
    #questions用来存放算术表达式
    continueTime = 0
    questions= []
    questions2 = []
    #answers用来存放算数表达式响应的答案
    answers=[]
    #生成所选运算符的序列
    operators=['+','-','×','÷']
    allOperators=['+','-','×','÷','(',')']
    #通过循环的方式随机生成算数表达式
    while len(answers) < n:
        #此处的意思为随机产生运算符的个数
        operatorNum = random.randint(1,3)
        #当为一个运算符的时候
        if operatorNum == 1:
            list = []
            num1 = genarateNumber(r)
            num2 = genarateNumber(r)
            operator = random.choice(operators)
            #将生成的数存在列表中
            list.append(num1)
            list.append(operator)
            list.append(num2)
            #构造算数表达式
            list = addBracket(operatorNum, list)
            listNew = standardFraction(list, allOperators)
            # 为算数表达式添加空格
            question1 = addBlank(list)
            question2 = addBlank(listNew)
            # 异常处理，如果出现/0的情况就认为这道题出错了，就会使本次生成结束，并开始新一轮生成
            temp = question1.replace('×', '*').replace('÷', '/')
            try:

                answer = Fraction(eval(temp)).limit_denominator()
            except ZeroDivisionError:
                continue
            #如果答案的结果大于前面命令行给定的范围，或者使负数，那么该情况不合理，也将社区
            if answer < 0 or answer > r or answer.denominator > 10:
                continue
            answerStr = str(answer)
            #将符合条件的算数表达式以及答案存入questions以及answers列表中，下面也如此
            questions.append(question2)
            questions2.append(question1)
            answers.append(answerStr)
        if operatorNum == 2:
            list =[]
            num1 = genarateNumber(r)
            num2 = genarateNumber(r)
            num3 = genarateNumber(r)
            operator1 = str(random.choice(operators))
            operator2 = str(random.choice(operators))
            list.append(num1)
            list.append(operator1)
            list.append(num2)
            list.append(operator2)
            list.append(num3)
            #为列表添加括号
            list = addBracket(operatorNum,list)
            listNew = standardFraction(list, allOperators)
            #为算数表达式添加空格
            question1 = addBlank(list)
            question2 = addBlank(listNew)
            temp = question1.replace('×', '*').replace('÷', '/')
            #异常处理，如果出现/0的情况就认为这道题出错了，就会使本次生成结束，并开始新一轮生成
            try:
                answer = Fraction(eval(temp)).limit_denominator()
            except ZeroDivisionError:
                continue
            #如果答案小于0或者大于命令行所规定的范围的话，就会认为这道题不符合要求，也会重新生成题目
            if answer < 0 or answer > r or answer.denominator > 10:
                continue
            answerStr = str(answer)
            questions.append(question2)
            questions2.append(question1)
            answers.append(answerStr)
        if operatorNum == 3:
            list = []
            num1 = genarateNumber(r)
            num2 = genarateNumber(r)
            num3 = genarateNumber(r)
            num4 = genarateNumber(r)
            operator1 = str(random.choice(operators))
            operator2 = str(random.choice(operators))
            operator3 = str(random.choice(operators))
            list.append(num1)
            list.append(operator1)
            list.append(num2)
            list.append(operator2)
            list.append(num3)
            list.append(operator3)
            list.append(num4)
            # 为列表添加括号
            list = addBracket(operatorNum, list)
            listNew = standardFraction(list,allOperators)
            # 为算数表达式添加空格

            question1 = addBlank(list)
            question2 = addBlank(listNew)

            #下面是之前调试代码用的print函数
            #print('question',question)
            # 异常处理，如果出现/0的情况就认为这道题出错了，就会使本次生成结束，并开始新一轮生成
            temp = question1.replace('×', '*').replace('÷', '/')
            try:
                answer = Fraction(eval(temp)).limit_denominator()
            except ZeroDivisionError:
                continue
            # 如果答案小于0或者大于命令行所规定的范围的话，就会认为这道题不符合要求，也会重新生成题目
            if answer < 0 or answer > r or answer.denominator>10:
                continue
            answerStr = str(answer)
        # 上面生成算术表达式大同异，下面代码可以判断跟之前生成的表达式是否等价。
        #设定两个关系，1.如果生成的answer值和之前answers钟所存的值有相等的
                    #2.同时，前面的式子去掉括号以及空格之后再排序后相等
        #当满足如上俩关系的时候，认为表达式等价
        questionSwitch = False
        answerSwitch = False
        questions2Temp=[]
        #对questions的quetsions变成可以比较是否等价的1样子
        for i in range(len(questions2)):
            questions2Temp.append(''.join(sorted(questions2[i].replace('(','').replace(')','').replace(' ',''))))
        if answerStr in answers:
            answerSwitch = True
        if ''.join(sorted(question1.replace('(','').replace(')','').replace(' ',''))) in questions2Temp:
            questionSwitch = True
        if questionSwitch == True and answerSwitch == True:
                #print('作废',continueTime)
            continueTime +=1
            continue
            #如果生成的式子等价太多的话，就说明你生成的范围太小了，数目太大了
        if continueTime >=10000:
            raise Exception("you have input too large number and two small range")
        questions.append(question2)
        questions2.append(question1)
        answers.append(answerStr)
    # 下面是将questions 和 answers 分别写入文件操作
    #首先定义两个新的列表，来存放
    #if
    #print(questions2)
    #print(answers)
    questionsNew = []
    for i in range(len(questions)):
        #按照需求，将/变为'÷'，将*变成'×'
        dataNew = str(i + 1) + '. ' + questions[i] + '\n'
        dataNew = dataNew
        questionsNew.append(dataNew)
        #print(dataNew)
    answersNew = []
    for i in range(len(answers)):
        #通过循环将答案列表中的答案按照需求中给给的格式输出
        a = Fraction(eval(answers[i])).limit_denominator()
        if a.denominator != 1 and a.numerator > a.denominator:
            s = str(i+1) + ". " + str(a.numerator // a.denominator) + "'" + str(a - a.numerator // a.denominator)+'\n'
            answersNew.append(s)
        else:
            s = str(i+1) + ". " + str(a) + '\n'
            answersNew.append(s)

    #将列表中得到内容存入到.txt文件中
    fp1 = open('Exercises.txt','w')
    fp1.writelines(questionsNew)
    fp2 = open('Answers.txt','w')
    fp2.writelines(answersNew)
    fp1.close()
    fp2.close()
    for i in range(len(answers)):
       print(questionsNew[i],end = '')
       print(answersNew[i],end = '')
#需求2：生成成绩
def generateGrade(newExerciseFile,newAnswerFile):
    questions = []
    with open(newExerciseFile,'r') as file:
        #将问题文件读到列表中
        lines= file.readlines()
        #将列表中固定格式的算术表达式取出来，并变成标准的算术表达式格式
        for line in lines:
            line = line.replace("\n","")
            line = line.replace("÷", "/")
            line = line.replace("×", "*")
            line = line.split('. ')[1]
            questions.append(line)
    questionsNew = []
    for question in questions:
        tempsNew = []
        temps = question.split(' ')
        for i in range(len(temps)):

            if "'" in temps[i]:
                temp = Fraction(eval(temps[i].split("'")[1])).limit_denominator()
                temp = (temp + eval(temps[i].split("'")[0]))
                tempsNew.append(temp)
                #print(temp)
            else:
                tempsNew .append(temps[i])
        #print(temps)
       # print(tempsNew)
        questionsNew.append(str(addBlank(tempsNew)))
    #print(questionsNew)
    questions = questionsNew
    answersTrue = []

    #通过循环找出每个问题真的答案存入到answerTrue中
    for question in questions:
        answer = Fraction(eval(question)).limit_denominator()
        if answer.denominator != 1 and answer.numerator > answer.denominator:
            s = str(answer.numerator // answer.denominator) + "'" + str(answer - answer.numerator // answer.denominator)
            answersTrue.append(s)
        else:
            s= str(answer)
            answersTrue.append(s)
        #print(s,type(s))

    with open(newAnswerFile,'r') as file:
        answers=[]
        lines = file.readlines()
        #将答案文件的答案变成标准形式
        for line in lines:
            line = line.replace('\n','')
            line = line.split('. ')[1]
            answers.append(line)
            #print(line,type(line))
    #定义两个列表，存入正确的答案和错误的答案
    questionCorrect =[]
    questionWrong =[]
    #比较文件中答案和算出的正确对答案，相同则将题号存入questionCorrect,不同则存入questionWrong
    for i in range(len(questions)):
        if answersTrue[i] == answers[i]:
            questionCorrect.append((i+1))
        else:
            questionWrong.append((i+1))
    #print(questionWrong)
    #print(questionCorrect)
    #将信息转换成需求中的那种形式
    strCorrect = 'Correct: '+str(len(questionCorrect)) +' ('
    if len(questionCorrect) ==0 :
        strCorrect +=')'
    for i in range(len(questionCorrect)):
        if i == len(questionCorrect) - 1:
            strCorrect+= str(questionCorrect[i])+')'
        else:
            strCorrect+=str(questionCorrect[i])+', '

    strWrong = 'Wrong: ' + str(len(questionWrong)) + ' ('
    if len(questionWrong) == 0:
        strWrong+=')'
    for i in range(len(questionWrong)):
        if i == len(questionWrong) - 1:
            strWrong += str(questionWrong[i]) + ')'
        else:
            strWrong += str(questionWrong[i]) + ', '

    print(strCorrect)
    print(strWrong)
    with open ('Grade.txt','w') as file:
        strCorrect +='\n'
        file.writelines(strCorrect)
        file.writelines(strWrong)
