import time
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

#Function to carry out NSGA-II's fast non dominated sort
def fast_non_dominated_sort(list):
    S=[[] for i in range(0,len(list))]
    front = [[]]
    n=[0 for i in range(0,len(list))]
    rank = [0 for i in range(0, len(list))]

    for p in range(0,len(list)):
        S[p]=[]
        n[p]=0
        # 两个循环更新每个每个点的支配集合和被支配数量
        for q in range(0, len(list)):
            if mycompare(list[p],list[q])==1:
                if q not in S[p]:
                    S[p].append(q)
            elif mycompare(list[q],list[p])==1:
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)

    i = 0
    while(front[i] != []):
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)

    del front[len(front)-1]
    return front
# time_start=time.time()
# test=[[5.0, 35.0, 1.0, -8.0, -300.0, -3.85], [5.0, 55.0, 1.0, -15.0, -300.0, -26.5], [10.0, 77.0, 1.0, -8.0, -300.0, -7.08], [5.0, 8.0, 1.0, -15.0, -300.0, -33.55], [10.0, 100.0, 1.0, -30.0, -300.0, -28.39]]
# non_dominated_sorted_solution = fast_non_dominated_sort(test)
# print(non_dominated_sorted_solution)
# time_end=time.time()
# print("fast_non_dominated_sort花费的时间",time_end-time_start)

