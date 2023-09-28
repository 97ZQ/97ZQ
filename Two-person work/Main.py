import argparse
import os
from Method import generateQuestionAndAnswer
from Method import generateGrade
#首先实现命令行输入来实现对应的功能
parser = argparse.ArgumentParser()
group = parser.add_argument('-n','--numberNum',type=int,help='add your question numbers')
group = parser.add_argument('-r','--rangeNum',type=int,help='add your question range')
group = parser.add_argument('-e','--exerciseFile',help='read your question file')
group = parser.add_argument('-a','--answerFile',help='read your question answer file')
args = parser.parse_args()
print(type(args))
#处理异常，规定命令行的使得程序要么接受 -r -n 要么接受 -e -a
if (args.numberNum is None and args.rangeNum is None and args.exerciseFile is not None and args.answerFile is not None) \
    or (args.numberNum is not None and args.rangeNum is not None and args.exerciseFile is None and args.answerFile is None):
    #当输入的是-n -r 时
    if args.numberNum is not None:
        #使用户输入正确的命令行参数
        if args.numberNum <0 or args.rangeNum <0 :
            raise Exception('Please make your numberNum and rangeNum >=0')
        #在处理完异常之后，就进行第一个需求，生成相应数目的题目以及各自的答案，并将他们按照相应的形式存入文件中
        generateQuestionAndAnswer(args.rangeNum, args.numberNum)
    #当输入的是-e -a时
    if args.exerciseFile is not None:
        newExerciseFile = str(args.exerciseFile)
        newAnswerFile = str(args.answerFile)
        #查看所输入的文件是否存在，不存在的话抛出异常
        if not os.path.exists(newExerciseFile):
            raise (f'Not Found"{newExerciseFile}" File')
        if not os.path.exists(newAnswerFile):
            raise (f'Not Found"{newAnswerFile}" File')
        #基于所给定的文件newExerciseFile和newAnswerFile来给出计算的对错
        generateGrade(newExerciseFile,newAnswerFile)
#
# 如果输入的命令不是-r -n 或者 -a -e则抛出异常
else:
    raise Exception('Please input --help or your command with(python Main.py -n [int] -r[int]) or python Main.py (-e [str] -a [str])')
