import time
class mysort():
    # 比较函数 返回值为0，1，2分别代表相等，小于和大于
    def mycompare(a, b):
        result = [-1, -1, -1, -1, -1, -1]
        for i in range(6):
            if a[i] == b[i]:
                result[i] = 0
            elif a[i] < b[i]:
                result[i] = 1
            else:
                result[i] = 2
        # a支配b
        if (1 not in result) and (2 in result):
            return 1
        # b支配a
        elif (1 in result) and (2 not in result):
            return 2
        # a,b互不支配
        elif (1 in result) and (2 in result):
            return 3
        # a=b
        else:
            return 4



    def QuickSort(myList, start, end):
        # 判断low是否小于high,如果为false,直接返回
        # 设置一个数组存储需要删除的节点下标
        # remove_list = []
        if start < end:
            i, j = start, end
            # 设置基准数
            if myList[i]!=-1:
                base = myList[i]
            else:
                while myList[i]==-1:
                    i=i+1
                base=myList[i]
            # print(base)
            while i < j:
                # flag记录是否有比base大的值  设置两个flag监测是否已经符合要求
                flag0 = 0
                flag1 = 0
                # 设置一个参数记录更新的base位置 方便以后对该下标进行操作
                inter_base = i
                while (i < j):
                    if myList[i] == -1:
                        i = i + 1
                    else:
                        inter_value = mysort.mycompare(myList[i], base)
                        if inter_value == 4:
                            if start==i:
                                i=i+1
                                continue
                            else:
                                myList[i] = -1
                                i = i + 1
                        elif inter_value == 2:
                            flag1 = 1
                            myList[i] = -1
                            i = i + 1
                        #     当myList[i]和 base互不支配的时候 base不变
                        elif inter_value == 3:
                            # inter_base = i
                            break
                        else:
                            myList[start]=-1
                            base = myList[i]
                            inter_base = i
                            break
                # 如果列表后边的数,比基准数大,则前移一位直到有比基准数小的数出现
                while (i < j):
                    if myList[j] == -1:
                        j = j - 1
                    else:
                        inter_value = mysort.mycompare(myList[j], base)
                        if inter_value == 3 :
                            j = j - 1
                        elif inter_value == 4:
                            myList[j]=-1
                            j=j-1
                        elif inter_value == 1:
                            flag0 = 1
                            j = j - 1
                        else:
                            myList[j] = -1
                            j=j-1
                # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
                # myList[i] = myList[j]
                if flag0:
                    myList[inter_base] = -1
                if flag0 == 0 and flag1 == 0:
                    break
            # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
            # 递归前后半区

            mysort.QuickSort(myList, i, len(myList)-1)
        return myList
    def get_index(a):
        A=[]
        for i in range(len(a)):
            if a[i]!=-1:
                A.append(i)
        return A
# time_start=time.time()
# test=[[5.0, 35.0, 1.0, -8.0, -300.0, -3.85], [5.0, 55.0, 1.0, -15.0, -300.0, -26.5], [10.0, 77.0, 1.0, -8.0, -300.0, -7.08], [5.0, 8.0, 1.0, -15.0, -300.0, -33.55], [10.0, 100.0, 1.0, -30.0, -300.0, -28.39]]
# non_dominated_sorted_solution = mysort.get_index(mysort.QuickSort(test,0,len(test)-1))
# print(non_dominated_sorted_solution)
# time_end=time.time()
# print("fast_non_dominated_sort花费的时间",time_end-time_start)