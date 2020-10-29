# # 计算数据
#
import csv
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# # #
# #
# # 精确率
# ac=[0,0,0,0,0,0,0,0,0,0]
# t=[0,0,0,0,0,0,0,0,0,0]
# # ac=[0,0,0,0]
#
# # reader = csv.reader(open("top5.csv"))
# # for accuracy,time in reader:
# #     ac[0]=ac[0]+float(accuracy)
# #     # t[0]=t[0]+float(time)
# #
# # reader = csv.reader(open("top10.csv"))
# # for accuracy,time in reader:
# #     ac[1]=ac[1]+float(accuracy)
# #     # t[1]=t[1]+float(time)
# #
# # reader = csv.reader(open("top15.csv"))
# # for accuracy, time in reader:
# #     ac[2] = ac[2] + float(accuracy)
# #     # t[2] = t[2] + float(time)
# #
# # reader = csv.reader(open("top20.csv"))
# # for accuracy, time in reader:
# #     ac[3] = ac[3] + float(accuracy)
# #     # t[3] = t[3] + float(time)
#
# reader = csv.reader(open("top1.csv"))
# for accuracy,time in reader:
#     ac[0]=ac[0]+float(accuracy)
#     t[0]=t[0]+float(time)
#
# reader = csv.reader(open("top2.csv"))
# for accuracy,time in reader:
#     ac[1]=ac[1]+float(accuracy)
#     t[1]=t[1]+float(time)
#
# reader = csv.reader(open("top3.csv"))
# for accuracy, time in reader:
#     ac[2] = ac[2] + float(accuracy)
#     t[2] = t[2] + float(time)
#
# reader = csv.reader(open("top4.csv"))
# for accuracy, time in reader:
#     ac[3] = ac[3] + float(accuracy)
#     t[3] = t[3] + float(time)
#
# reader = csv.reader(open("top5.csv"))
# for accuracy, time in reader:
#     ac[4] = ac[4] + float(accuracy)
#     t[4] = t[4] + float(time)
#
# reader = csv.reader(open("top6.csv"))
# for accuracy, time in reader:
#     ac[5] = ac[5] + float(accuracy)
#     t[5] = t[5] + float(time)
#
# reader = csv.reader(open("top7.csv"))
# for accuracy, time in reader:
#     ac[6] = ac[6] + float(accuracy)
#     t[6] = t[6] + float(time)
#
# reader = csv.reader(open("top8.csv"))
# for accuracy, time in reader:
#     ac[7] = ac[7] + float(accuracy)
#     t[7] = t[7] + float(time)
#
#
# reader = csv.reader(open("top9.csv"))
# for accuracy, time in reader:
#     ac[8] = ac[8] + float(accuracy)
#     t[8] = t[8] + float(time)
#
# reader = csv.reader(open("top10.csv"))
# for accuracy,time in reader:
#     ac[9]=ac[9]+float(accuracy)
#     t[9]=t[9]+float(time)
#
# #
# for i in range(len(ac)):
#     ac[i]=ac[i]/13
#     t[i]=t[i]/13
# #
# print(ac)
# print(sum(t)/10)
# m=0
# n=0
# for i in range(len(t)):
#     m=m+t[i][0]
#     n = n + t[i][1]
#
# print(m/len(t))
# print(n/len(t))
#
# #
#
#
# # #
# # 响应时间
# t=[]
# reader1 = csv.reader(open("top5.csv"))
# for accuracy,time in reader1:
#     t.append(float(time))
#
# reader2 = csv.reader(open("top10.csv"))
# for accuracy,time in reader2:
#     t.append(float(time))
#
# reader3 = csv.reader(open("top15.csv"))
# for accuracy,time in reader3:
#     t.append(float(time))
#
#
#
# reader4 = csv.reader(open("top20.csv"))
# for accuracy,time in reader4:
#     t.append(float(time))
#
#
# print(sum(t)/len(t))


# #
# #
# #
# #
# #

#
# #
#
# # 响应时间
# import csv
# # -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# import numpy as np
# import random
# from matplotlib.font_manager import FontManager
# # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
# plt.figure(figsize=(8, 6), dpi=80)
#
# # 再创建一个规格为 1 x 1 的子图
# plt.subplot(1, 1, 1)
#
# # 柱子总数
# N = 3
# t_time=[0.219,0.553,1.086]
# t1_time=[12.701,13.327,14.254]
# t2_time=[3.989,8.916,19.932]
# t3_time=[0.216,0.421,0.965]
# t4_time=[0.2824, 0.29834,0.3418]
# # 包含每个柱子对应值的序列
# values = t_time
# values1 = t1_time
# values2 = t2_time
# values3 = t3_time
# values4=t4_time
#
# # 包含每个柱子下标的序列
# index = np.arange(N)
#
# # 柱子的宽度
# width = 0.15
#
# # 绘制柱状图, 每根柱子的颜色为紫罗兰色
# # p = plt.bar(index, values, width, label="TOPSIS",hatch='*')
# p = plt.bar(index, values, width, label="TOPSIS")
# p = plt.bar(index+width, values1, width, label="ES")
# p = plt.bar(index+2*width, values2, width, label="Dynamic Skyline")
# p = plt.bar(index+3*width, values3, width, label="Our(last)")
# p = plt.bar(index+4*width, values4, width, label="Our(now)")
#
#
# # 设置横轴标签
# plt.xlabel('The size of dataset')
# # 设置纵轴标签
# plt.ylabel('Time(s)')
#
# # 添加标题
# plt.title('The response time')
#
# # 添加纵横轴的刻度
# plt.xticks(index, (5,10,20))
# # plt.yticks(np.arange(0,10,1))
# plt.ylim((0,15))
#
# # 添加图例
# plt.legend(loc='center left', bbox_to_anchor=(0.05, -0.15),ncol=5)
#
# plt.show()


#
#
# #
#
# # 精确率
# import csv
# # -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# import numpy as np
# import random
# from matplotlib.font_manager import FontManager
# # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
# plt.figure(figsize=(8, 6), dpi=80)
#
# # 再创建一个规格为 1 x 1 的子图
# plt.subplot(1, 1, 1)
#
# # 柱子总数
# N = 4
#
# t_acc=[65.38461538461539, 62.30769230769231, 59.487179487179475, 58.65384615384615]
# t1_acc=[73.84615384615384, 69.61538461538461, 70.25641025641025, 69.61538461538461]
# t2_acc=[73.46153846153847, 66.53846153846153, 63.84615384615385, 59.03846153846154]
# t3_acc=[77.6923076923077, 76.92307692307692, 71.79487179461537, 70.1923076923077]
# t4_acc=[81.53,69.23,56.15,44.80]
#
#
# # 包含每个柱子对应值的序列
# values = t_acc
# values1 = t1_acc
# values2 = t2_acc
# values3 = t3_acc
# values4=t4_acc
#
# # 包含每个柱子下标的序列
# index = np.arange(N)
#
# # 柱子的宽度
# width = 0.15
#
# # 绘制柱状图, 每根柱子的颜色为紫罗兰色
# # p = plt.bar(index, values, width, label="TOPSIS",hatch='*')
# p = plt.bar(index, values, width, label="TOPSIS")
# p = plt.bar(index+width, values1, width, label="ES")
# p = plt.bar(index+2*width, values2, width, label="Dynamic Skyline")
# p = plt.bar(index+3*width, values3, width, label="Our(last)")
# p = plt.bar(index+4*width, values4, width, label="Our(now)")
#
#
# # 设置横轴标签
# plt.xlabel('The number of recommended sensor')
# # 设置纵轴标签
# plt.ylabel('The precision ratio(%)')
#
# # 添加标题
# plt.title('The precision ratio')
#
# # 添加纵横轴的刻度
# plt.xticks(index, (5,10,15,20))
# # plt.yticks(np.arange(0,10,1))
# plt.ylim((0,90))
#
# # 添加图例
# plt.legend(loc='center left', bbox_to_anchor=(0.05, -0.15),ncol=5)
#
# plt.show()
#


# # 折线图
# from pylab import *
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# x_axis_data = ["5%", "10%","15%","20%","25%","30%","35%"]
# # y_axis_data = [1.977,1.835,1.7899,1.7604,1.6919,1.6394,1.5673]
# y_axis_data = [61.17,58.56,56.21,54.01,52.18,49.57,48.32]
#
#
# # plot中参数的含义分别是横轴值，纵轴值，颜色，透明度和标签
# plt.plot(x_axis_data, y_axis_data, 'ro-', color='#4169E1', alpha=0.8)
#
# # 显示标签，如果不加这句，即使加了label='一些数字'的参数，最终还是不会显示标签
# plt.legend(loc="upper right")
# plt.xlabel('Matrix Density')
# plt.ylabel('MAE')
# plt.title('Throughput')
#
# plt.show()
# # plt.savefig('demo.jpg')  # 保存该图片
