import random

from utils import outputscreen



count = int(input('请输入题目数量:')) # 用户输入的 题目数量

questions = [] # 题目列表
answers = [] # 答案列表
# 初始化 题目列表 和 答案列表
# 题目列表 和 答案列表 是一一对应的，即 题目列表中的第i题的 答案 就是 答案列表的第i项；
for i in range(0,count):
    a = random.randint(1,20) # 第一个数字（从1到20之间随机一整数）
    b = random.randint(1,20) # 第二个数字（从1到20之间随机一整数）
    op = random.choice(['+','-']) # 运算符（+或-）
    quest = '%d %s %d = '%(a,op,b) # 题目形式 a _ b = 
    ans = 0 # 题目答案
    questions.append(quest) # 将题目加入到 题目列表
    # 计算题目答案
    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    answers.append(ans) # 将答案加入到 答案列表

correctCount = 0 # 答对题目的个数，初始化为0
#遍历所有题目
for i in range(0,count):
    a = int(input(questions[i])) # 显示题目并接收用户输入的答案
    if a == answers[i]:
        correctCount += 1
        # print("Yes, your answer is right.")
        outputscreen.green("回答正确。")
    else:
        # print("No, your answer is wrong.")    
        outputscreen.red("回答错误，正确答案是：%d。"%(answers[i]))    

# 打分
score = 100 * (correctCount/count)
# 写评价
pingjia = "优秀"
if score==100:
    pingjia = "优秀"
elif score >=80 and score < 100 :
    pingjia = "良好"
elif score >=60 and score < 80:
    pingjia = "及格"
else:
    pingjia = "不及格"    

# 输出结果
outputscreen.yellow("成绩：共%d题，答对%d题，得分：%d，评价：%s。"%(count,correctCount,score,pingjia))    