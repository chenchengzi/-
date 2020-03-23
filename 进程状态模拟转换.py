# coding=utf-8
import random
import time
resource1=3
resource2=3
ready = []  # 就绪状态队列
block = []  # 阻塞状态队列
creat= [] #   创建状态队列
def paixu(list, lens):  # 按优先级排序
    temp = []
    for j in range(0, lens):
        for k in range(0, lens - j - 1):
            if list[k][3] < list[k + 1][3]:
                temp = list[k]
                list[k] = list[k + 1]
                list[k + 1] = temp
def creat_new():
        global resource1,resource2
        print('*******进程获得了执行所需的资源******')
        # print('创建一个进程前，资源1为%d，资源2剩余%d' % (a, b))

        # print(resource1,resource2)
        resource1 =resource1- need1
        resource2 =resource2- need2
       # print(need1,need2)
       # print(resource1, resource2)
        # print('创建一个进程后，资源1剩余%d，资源2剩余%d'%(resource1,resource2))
        counter = random.randint(1, 8)  # 随机产生进程执行所 需的时间片
        priority = random.randint(1, 30)  # 优先级随机产生范围为1-30
        id = creat[0]+1
        zhouzhuan = []  # 周转时间列表，用于保存进程每次执行开始的时间
        state = 0
        io = random.randint(0, 1)  # 进程是否需要io
        print('----正在创建标号为%d的进程----' % (creat[0] + 1))
        #time.sleep(0.5)
        print('----进 程 创 建 成 功----')
        del creat[0]
        #time.sleep(0.5)
        task = [id, state, priority, counter, zhouzhuan, io, need1, need2]  # 建立进程列表
        ready.append(task)
        print('该进程已加入就绪队列中，此时就绪队列中的进程数为%d\n' % (len(ready)))
        #time.sleep(0.5)

def show_num():
        print('***此时就绪队列中的进程数为%d***' % (len(ready)))
        print('***此时阻塞队列中的进程数为%d***' % (len(block)))
        print('***此时处于创建状态的进程数为%d***\n'%(len(creat)))

def jiance():
    global resource1, resource2
    global need1,need2


    while len(creat)>0:
        need1 = random.randint(0, 2)  # 定义进程执行需要的第一种系统资源
        need2 = random.randint(0, 2)  # 定义进程执行需要的第二种系统资源
        print('需求A:%d,资源A:%d' % (need1, resource1))
        print('需求B:%d,资源B:%d' % (need2, resource2))
        if (need1 <= resource1 and need2 <=resource2):
            creat_new()
            print('创建一个进程后，资源A剩余%d，资源B剩余%d' % (resource1, resource2))
        else:
            print('资源再次不足，等待系统再次释放资源')
            show_num()
            break
def io(ready,block):
    for every in block:
        if every[5]==0:
            every[5]=int(input('请为标号为%d的进程执行I/O操作（输入1）：'%every[0]))
            if every[5]==1:
                print("☆☆☆进程状态转换---I/O完成☆☆☆")
                print('进程%d的I/O请求完成，由阻塞队列调入就绪队列'%every[0])
                ready.append(every)
            else:
                print('执行I/O请求失败')
        else:
            continue

num = int(input("请输入要创建的进程数目："))
for i in range (num):
    creat.append(i)
for i in range(len(creat)):
    print ('申请创建新的进程。。。。。')
    time.sleep(1)
    need1 = random.randint(0, 2)  # 定义进程执行需要的第一种系统资源
    need2 = random.randint(0, 2)  # 定义进程执行需要的第二种系统资源
    # print('需求A:%d,资源A:%d' % (need1, resource1))
    # print('需求B:%d,资源B:%d' % (need2, resource2))
    if (need1 <= resource1 and need2 <= resource2):
        creat_new()
        # print('创建一个进程后，资源A剩余%d，资源B剩余%d' % (resource1, resource2))

    else:
        print('资源不足创建新的进程，等待系统释放资源\n')
        show_num()
        break

paixu(ready,len(ready))

print('******进程调度开始：******')
time=0
while len(ready)>0:
    if (ready[0][3] > 0):
        print("☆☆☆进程状态转换---进程调度☆☆☆")
        print('进程%d由就绪态转换为执行态' % (ready[0][0]))
        print('当前时间是' + str(time))
        ready[0][4].append(time)  # 将进程每次开始运行时间加入周转列表
        print('该进程开始的时间是' + str(ready[0][4][0]))
        time += 3  # 每个时间片为3
        ready[0][3] -= 3  # 执行一次后进程时间片减3
        if (ready[0][3] > 0 and ready[0][5] == 0):
            print("☆☆☆进程状态转换---I/O请求☆☆☆")
            print('该进程执行IO请求，将被调入阻塞队列')
            block.append(ready[0])
            del ready[0]
            if len(ready)==0:
                io(ready,block)
        elif (ready[0][3] > 0):
            print("☆☆☆进程状态转换---时间片用完☆☆☆")
            print('进程标号为%d的进程第一个时间片已用完，将等待下一个时间片继续运行' % (ready[0][0]))     #时间片用完进程状态改变
            ready.append(ready[0])
            del ready[0]
            print('标号为%d的进程添加到就绪队列尾部成功\n' % (ready[-1][0]))
            io(ready,block)
        else:
            print("☆☆☆进程状态转换---执行完毕舍弃进程☆☆☆")
            print("\n标号为%d进程时间片用完,周转时间为%d将被终止" % (ready[0][0], ready[0][4][-1] - ready[0][4][0] + ready[0][
                3] + 3))  # 周转时间= 进程最后一次执行的开始时间-进程第一次执行的开始时间+最后一次执行时剩余的时间片
            print('该进程所占用的系统资源被释放')
            resource1+= ready[0][6]
            resource2+=ready[0][7]
            del ready[0]
            jiance( )
            io(ready,block)
print("所有进程执行完毕！！！")

