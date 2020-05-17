#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import json
import xlwt
top_idx = 500 # 考虑前500个最常出现的字


def get_data(path):
    all_name = []
    with open(path,'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            full_name = line.strip()
            all_name.append(full_name)
            # print(line.strip())
    return all_name

def analysis_ancient_name(path):
    data = get_data(path)
    all_chart = {}
    for name in data:
        # print(name)
        for charter_idx in range(1,len(name)):
            if name[charter_idx] not in all_chart:
                all_chart[name[charter_idx]] = 1
            else:
                all_chart[name[charter_idx]] +=1
    sort_charter = sorted(all_chart.items(), key=lambda x: x[1], reverse=True)
    rest_chater = sort_charter[top_idx:]
    rest_ancient_list = []
    for key in rest_chater:
        rest_ancient_list.append(key[0])
    sort_charter = sort_charter[:top_idx]

    with open('charter.json', 'w', encoding='utf-8') as json_write:
        json.dump(sort_charter, json_write, indent=4, ensure_ascii=False)
    return sort_charter,rest_ancient_list

def analysis_modern_name(path):
    data = get_data(path)
    all_chart = {}
    for name in data:
        # print(name)
        for charter_idx in range(1, len(name)):
            if name[charter_idx] not in all_chart:
                all_chart[name[charter_idx]] = 1
            else:
                all_chart[name[charter_idx]] += 1
    sort_charter = sorted(all_chart.items(), key=lambda x: x[1], reverse=True)
    sort_charter = sort_charter[:top_idx]
    with open('modern_charter.json', 'w', encoding='utf-8') as json_write:
        json.dump(sort_charter, json_write, indent=4, ensure_ascii=False)
    return sort_charter


def sele_comment(ancient, modern):
    ancient_list = []
    modern_list = []
    comment = []
    for key in ancient:
        ancient_list.append(key[0])
    for tmp in modern:
        modern_list.append(tmp[0])
        if tmp[0] in ancient_list:
            comment.append(tmp[0])

    # comment = list(set(ancient_list).union(set(modern_list)))
    # print(ancient_list)
    # print(modern_list)
    print(comment)
    return ancient_list,modern_list,comment

def save_excel(data_list,index):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')

    # 写入excel
    # 参数对应 行, 列, 值
    for idx in range(len(data_list)):
        worksheet.write(idx, index, data_list[idx])

    # 保存
    workbook.save('Excel_test'+ str(index) +'.xls')

if __name__ =='__main__':
    path = './Chinese_Names_Corpus/Ancient_Names_Corpus（25W）.txt'
    ancient,rest_ancient = analysis_ancient_name(path)

    path2 = './Chinese_Names_Corpus/Chinese_Names_Corpus（120W）.txt'
    modern = analysis_modern_name(path2)

    ancient_list, modern_list, comment =sele_comment(ancient, modern)
    ancient_rest,modern_rest = [],[]
    for tmp in ancient_list:
        if tmp not in comment:
            ancient_rest.append(tmp)
    for tmp2 in modern_list:
        if tmp2 not in comment:
            modern_rest.append(tmp2)

    # save_excel(ancient_rest,1)
    # save_excel(modern_rest,2)
    # save_excel(comment,3)
    save_excel(rest_ancient,4)