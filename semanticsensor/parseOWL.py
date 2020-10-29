import rdflib
import re
from rdflib import Namespace,RDF
from rdflib import URIRef, Literal
from rdflib.namespace import XSD
import csv
import xlsxwriter

# newg1=rdflib.Graph()
# newg2=rdflib.Graph()
# newg3=rdflib.Graph()
# newg4=rdflib.Graph()
g1 = rdflib.Graph()
g2 = rdflib.Graph()
g3 = rdflib.Graph()
g4 = rdflib.Graph()
g5 = rdflib.Graph()
# g6 = rdflib.Graph()
# g7 = rdflib.Graph()
# g8 = rdflib.Graph()
# g9 = rdflib.Graph()
# g10 = rdflib.Graph()
# g11 = rdflib.Graph()
# g12 = rdflib.Graph()
# g13 = rdflib.Graph()
# g14 = rdflib.Graph()
# g15 = rdflib.Graph()
# g16 = rdflib.Graph()
# g17 = rdflib.Graph()
# # g18 = rdflib.Graph()
# g19 = rdflib.Graph()
# g20 = rdflib.Graph()




# newg1.parse("./data/newrdf1.owl", format="xml")
# newg2.parse("./data/newrdf2.owl", format="xml")
# newg3.parse("./data/newrdf3.owl", format="xml")
# newg4.parse("./data/newrdf4.owl", format="xml")
g1.parse("./data/owl1.owl", format="xml")
g2.parse("./data/owl2.owl", format="xml")
g3.parse("./data/owl3.owl", format="xml")
g4.parse("./data/owl4.owl", format="xml")
g5.parse("./data/owl5.owl", format="xml")
# g6.parse("./data/owl6.owl", format="xml")
# g7.parse("./data/owl7.owl", format="xml")
# g8.parse("./data/owl8.owl", format="xml")
# g9.parse("./data/owl9.owl", format="xml")
# g10.parse("./data/owl10.owl", format="xml")
# g11.parse("./data/owl11.owl", format="xml")
# g12.parse("./data/owl12.owl", format="xml")
# g13.parse("./data/owl13.owl", format="xml")
# g14.parse("./data/owl14.owl", format="xml")
# g15.parse("./data/owl15.owl", format="xml")
# g16.parse("./data/owl10.owl", format="xml")
# g17.parse("./data/owl11.owl", format="xml")
# g18.parse("./data/owl12.owl", format="xml")
# g19.parse("./data/owl13.owl", format="xml")
# g20.parse("./data/owl14.owl", format="xml")

ns = Namespace('xmlns="http://www.semanticweb.org/zhaoqian/ontologies/2019/8/untitled-ontology-8#')  # 命名空间


# 创建和写入文件
def create__file(file_path,msg):
    with open(file_path, "a+", encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for i in msg:
            writer.writerow(i)
    csvfile.close


# 写入表格
def write_to_table(table_path,table):

    workbook = xlsxwriter.Workbook(table_path)  # 创建一个excel文件
    worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1

    # worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
    # bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象

    worksheet.write('A1', U'传感器类型')
    worksheet.write('B1', U'属性')
    worksheet.write('C1', U'最小值')
    worksheet.write('D1', U'最大值')
    worksheet.write('E1', U'标识')
    # i代表传感器类型
    # 设置参数统计行数
    m=0
    for i in table.keys():
        # j代表传感器类型对应的属性字典
        for j in table[i].keys():
            worksheet.write(m, 0,i)
            worksheet.write(m, 1, j)
            worksheet.write(m, 2, table[i][j][0])
            worksheet.write(m, 3, table[i][j][1])
            worksheet.write(m, 4, table[i][j][2])
            m=m+1
    workbook.close()

# 1、第一阶段


rdftype = URIRef("http://www.semanticweb.org/zhaoqian/ontologies/2019/8/untitled-ontology-8#sensor_type")
#获取RDF数据中传感器的类型

types=[]
# 表格记录传感器属性及范围
table={}
for _,_,o in g1.triples((None,rdftype,None)):
    if o not in types:
        types.append(o)


# 根据类型遍历数据分类传感器，将不同类型的传感器存储在不同的文件中，并维护一个字典记录传感器类型和属性的取值范围
for i in types:
    intertable={}
    print(i)
    interdata=[]
# #    获取传感器名称
#     for s in newg1.subjects(rdftype,i):
#         # 根据传感器名称获取传感器三元组
#         for a,b,c in newg1.triples((s,None,None)):
#             interdata.append([Literal(a), Literal(b), Literal(c)])
#             if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
#                continue
#             else:
#                 if b not in intertable.keys():
#                     if b.split('#')[-1] in ['lon', 'lat']:
#                         intertable[b] = [Literal(c), Literal(c),0]
#                     elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
#                         intertable[b] = [Literal(c), Literal(c),-1]
#                     elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
#                         intertable[b] = [Literal(c), Literal(c),1]
#                 else:
#                     if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
#                         intertable[b][0]=Literal(float(c),datatype=XSD.float)
#                     elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
#                         intertable[b][1]=Literal(float(c),datatype=XSD.float)
#                     else:
#                         continue
#
#     for s in newg2.subjects(rdftype,i):
#         # 根据传感器名称获取传感器三元组
#         for a,b,c in newg2.triples((s,None,None)):
#             interdata.append([Literal(a), Literal(b), Literal(c)])
#             if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
#                continue
#             else:
#                 if b not in intertable.keys():
#                     if b.split('#')[-1] in ['lon', 'lat']:
#                         intertable[b] = [Literal(c), Literal(c),0]
#                     elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
#                         intertable[b] = [Literal(c), Literal(c),-1]
#                     elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
#                         intertable[b] = [Literal(c), Literal(c),1]
#                 else:
#                     if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
#                         intertable[b][0]=Literal(float(c),datatype=XSD.float)
#                     elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
#                         intertable[b][1]=Literal(float(c),datatype=XSD.float)
#                     else:
#                         continue
#
#
#
#     for s in newg3.subjects(rdftype,i):
#         # 根据传感器名称获取传感器三元组
#         for a,b,c in newg3.triples((s,None,None)):
#             interdata.append([Literal(a), Literal(b), Literal(c)])
#             if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
#                continue
#             else:
#                 if b not in intertable.keys():
#                     if b.split('#')[-1] in ['lon', 'lat']:
#                         intertable[b] = [Literal(c), Literal(c),0]
#                     elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
#                         intertable[b] = [Literal(c), Literal(c),-1]
#                     elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
#                         intertable[b] = [Literal(c), Literal(c),1]
#                 else:
#                     if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
#                         intertable[b][0]=Literal(float(c),datatype=XSD.float)
#                     elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
#                         intertable[b][1]=Literal(float(c),datatype=XSD.float)
#                     else:
#                         continue
#
#
#
#     for s in newg4.subjects(rdftype,i):
#         # 根据传感器名称获取传感器三元组
#         for a,b,c in newg4.triples((s,None,None)):
#             interdata.append([Literal(a), Literal(b), Literal(c)])
#             if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
#                continue
#             else:
#                 if b not in intertable.keys():
#                     if b.split('#')[-1] in ['lon', 'lat']:
#                         intertable[b] = [Literal(c), Literal(c),0]
#                     elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
#                         intertable[b] = [Literal(c), Literal(c),-1]
#                     elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
#                         intertable[b] = [Literal(c), Literal(c),1]
#                 else:
#                     if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
#                         intertable[b][0]=Literal(float(c),datatype=XSD.float)
#                     elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
#                         intertable[b][1]=Literal(float(c),datatype=XSD.float)
#                     else:
#                         continue


    for s in g1.subjects(rdftype,i):
        # 根据传感器名称获取传感器三元组
        for a,b,c in g1.triples((s,None,None)):
            interdata.append([Literal(a), Literal(b), Literal(c)])
            if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
               continue
            else:
                if b not in intertable.keys():
                    if b.split('#')[-1] in ['lon', 'lat']:
                        intertable[b] = [Literal(c), Literal(c),0]
                    elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
                        intertable[b] = [Literal(c), Literal(c),-1]
                    elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
                        intertable[b] = [Literal(c), Literal(c),1]
                else:
                    if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
                        intertable[b][0]=Literal(float(c),datatype=XSD.float)
                    elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
                        intertable[b][1]=Literal(float(c),datatype=XSD.float)
                    else:
                        continue


    for s in g2.subjects(rdftype,i):
        # 根据传感器名称获取传感器三元组
        for a,b,c in g2.triples((s,None,None)):
            interdata.append([Literal(a), Literal(b), Literal(c)])
            if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
               continue
            else:
                if b not in intertable.keys():
                    if b.split('#')[-1] in ['lon', 'lat']:
                        intertable[b] = [Literal(c), Literal(c),0]
                    elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
                        intertable[b] = [Literal(c), Literal(c),-1]
                    elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
                        intertable[b] = [Literal(c), Literal(c),1]
                else:
                    if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
                        intertable[b][0]=Literal(float(c),datatype=XSD.float)
                    elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
                        intertable[b][1]=Literal(float(c),datatype=XSD.float)
                    else:
                        continue
    #
    #
    #
    for s in g3.subjects(rdftype,i):
        # 根据传感器名称获取传感器三元组
        for a,b,c in g3.triples((s,None,None)):
            interdata.append([Literal(a), Literal(b), Literal(c)])
            if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
               continue
            else:
                if b not in intertable.keys():
                    if b.split('#')[-1] in ['lon', 'lat']:
                        intertable[b] = [Literal(c), Literal(c),0]
                    elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
                        intertable[b] = [Literal(c), Literal(c),-1]
                    elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
                        intertable[b] = [Literal(c), Literal(c),1]
                else:
                    if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
                        intertable[b][0]=Literal(float(c),datatype=XSD.float)
                    elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
                        intertable[b][1]=Literal(float(c),datatype=XSD.float)
                    else:
                        continue
    #
    for s in g4.subjects(rdftype,i):
        # 根据传感器名称获取传感器三元组
        for a,b,c in g4.triples((s,None,None)):
            interdata.append([Literal(a), Literal(b), Literal(c)])
            if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
               continue
            else:
                if b not in intertable.keys():
                    if b.split('#')[-1] in ['lon', 'lat']:
                        intertable[b] = [Literal(c), Literal(c),0]
                    elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
                        intertable[b] = [Literal(c), Literal(c),-1]
                    elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
                        intertable[b] = [Literal(c), Literal(c),1]
                else:
                    if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
                        intertable[b][0]=Literal(float(c),datatype=XSD.float)
                    elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
                        intertable[b][1]=Literal(float(c),datatype=XSD.float)
                    else:
                        continue


    for s in g5.subjects(rdftype,i):
        # 根据传感器名称获取传感器三元组
        for a,b,c in g5.triples((s,None,None)):
            interdata.append([Literal(a), Literal(b), Literal(c)])
            if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
               continue
            else:
                if b not in intertable.keys():
                    if b.split('#')[-1] in ['lon', 'lat']:
                        intertable[b] = [Literal(c), Literal(c),0]
                    elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
                        intertable[b] = [Literal(c), Literal(c),-1]
                    elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
                        intertable[b] = [Literal(c), Literal(c),1]
                else:
                    if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
                        intertable[b][0]=Literal(float(c),datatype=XSD.float)
                    elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
                        intertable[b][1]=Literal(float(c),datatype=XSD.float)
                    else:
                        continue



    #
    # for s in g6.subjects(rdftype,i):
    #     # 根据传感器名称获取传感器三元组
    #     for a,b,c in g6.triples((s,None,None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
    #            continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c),0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c),-1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c),1]
    #             else:
    #                 if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
    #                     intertable[b][0]=Literal(float(c),datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1]=Literal(float(c),datatype=XSD.float)
    #                 else:
    #                     continue





    # for s in g7.subjects(rdftype,i):
    #     # 根据传感器名称获取传感器三元组
    #     for a,b,c in g7.triples((s,None,None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
    #            continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c),0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c),-1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c),1]
    #             else:
    #                 if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
    #                     intertable[b][0]=Literal(float(c),datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1]=Literal(float(c),datatype=XSD.float)
    #                 else:
    #                     continue
    #
    #
    #
    #

    # for s in g8.subjects(rdftype,i):
    #     # 根据传感器名称获取传感器三元组
    #     for a,b,c in g8.triples((s,None,None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
    #            continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c),0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c),-1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c),1]
    #             else:
    #                 if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
    #                     intertable[b][0]=Literal(float(c),datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1]=Literal(float(c),datatype=XSD.float)
    #                 else:
    #                     continue
    #

    #
    # for s in g9.subjects(rdftype,i):
    #     # 根据传感器名称获取传感器三元组
    #     for a,b,c in g9.triples((s,None,None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
    #            continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c),0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c),-1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c),1]
    #             else:
    #                 if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
    #                     intertable[b][0]=Literal(float(c),datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1]=Literal(float(c),datatype=XSD.float)
    #                 else:
    #                     continue
    #
    #


    # for s in g10.subjects(rdftype,i):
    #     # 根据传感器名称获取传感器三元组
    #     for a,b,c in g10.triples((s,None,None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type','hasAddress','type','sensor_name']:
    #            continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c),0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time','the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c),-1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c),1]
    #             else:
    #                 if Literal(float(c),datatype=XSD.float) < Literal(float(intertable[b][0]),datatype=XSD.float):
    #                     intertable[b][0]=Literal(float(c),datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1]=Literal(float(c),datatype=XSD.float)
    #                 else:
    #                     continue
    # for s in g11.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g11.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g12.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g12.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g13.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g13.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue

    # for s in g14.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g14.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g15.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g15.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    #
    # for s in g16.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g16.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g17.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g17.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g18.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g18.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g19.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g19.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue
    #
    # for s in g20.subjects(rdftype, i):
    #     # 根据传感器名称获取传感器三元组
    #     for a, b, c in g20.triples((s, None, None)):
    #         interdata.append([Literal(a), Literal(b), Literal(c)])
    #         if b.split('#')[-1] in ['sensor_type', 'hasAddress', 'type', 'sensor_name']:
    #             continue
    #         else:
    #             if b not in intertable.keys():
    #                 if b.split('#')[-1] in ['lon', 'lat']:
    #                     intertable[b] = [Literal(c), Literal(c), 0]
    #                 elif b.split('#')[-1] in ['the_startup_time', 'the_response_time', 'the_energy_consumption']:
    #                     intertable[b] = [Literal(c), Literal(c), -1]
    #                 elif b.split('#')[-1] in ['life', 'accuracy_of_measurement', 'sensitivity']:
    #                     intertable[b] = [Literal(c), Literal(c), 1]
    #             else:
    #                 if Literal(float(c), datatype=XSD.float) < Literal(float(intertable[b][0]), datatype=XSD.float):
    #                     intertable[b][0] = Literal(float(c), datatype=XSD.float)
    #                 elif Literal(float(c), datatype=XSD.float) > Literal(float(intertable[b][1]), datatype=XSD.float):
    #                     intertable[b][1] = Literal(float(c), datatype=XSD.float)
    #                 else:
    #                     continue

    table[i]=intertable
    create__file("./data/"+i+".csv", interdata)
# 写入表格
write_to_table("./data/table3.xlsx",table)
print(table)


# 2、第二阶段
# 构建检索图和数据图




