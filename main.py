# -*- coding = utf-8 -*-
# @Time  :2021/10/13 2:57 下午
# @Author  : Ruin
# @File  :main.py
# @software: PyCharm

import numpy as np
import pandas    as pd


def Smith_Waterman(str1, str2):  # s_score, m_score
    len1, len2 = len(str1), len(str2)

    # initialize the socre matrix
    matrix = np.zeros([len1 + 1, len2 + 1])
    for i in range(len1):
        matrix[i, 0] = 0
    for i in range(len2):
        matrix[0, i] = 0

    Space_punish = 0

    # score the matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            Skj = matrix[i - 1, j] - Space_punish
            Sik = matrix[i, j - 1] - Space_punish
            Sij = matrix[i - 1, j - 1] + 3 if str1[i - 1] == str2[j - 1] else matrix[i - 1, j - 1] - 3
            matrix[i, j] = max(Skj, Sik, Sij, 0)
    match_str1, match_str2, match_rate = Trace_back(str1, str2, matrix, Space_punish)
    return match_str1, match_str2, match_rate


def Trace_back(str1, str2, M, Space_punish):
    x, y = np.where(M == np.max(M))
    x, y = x[0], y[0]

    match_str1, match_str2 = "", ""
    match_count = 0
    score = 0
    count = 0
    while M[x, y] != 0:
        count += 1
        if M[x - 1, y] - Space_punish == M[x, y]:
            x = x - 1
            match_str1, match_str2 = str1[x] + match_str1, '_' + match_str2

            score += 0.5
        elif M[x, y - 1] - Space_punish == M[x, y]:
            y = y - 1

            match_str1, match_str2 = '_' + match_str1, str2[y] + match_str2
            score += 0.5
        else:
            x, y = x - 1, y - 1
            match_str1, match_str2 = str1[x] + match_str1, str2[y] + match_str2
            match_count += 1
            score += 1
    return match_str1, match_str2, score / count

def paper_compare(paper_list):

    for i in range(len(paper_list)-1):
        count = 0
        for j in range(i+1, len(paper_list)):

            Smith_Waterman(paper_list[i], paper_list[j])
            count += 1
        print("paper", i+1, "比较了", count, "次")

        return Smith_Waterman(paper_list[i], paper_list[j])



if __name__ == '__main__':
    with open("pt1.txt") as f:
        str1 = f.read()
    with open("pt2.txt") as f:
        str2 = f.read()
    with open("paper3.txt") as f:
        str3 = f.read()
    paper_list = [str1, str2]
    pla1, pla2, socre = paper_compare(paper_list)
    print(pla1, pla2, socre)


    #data = [['paper1', repeat1, score]]
    #paper1 = pd.DataFrame(data, columns=['name', 'rep_to_p2', 'score'])
    #print(paper1)


    # implement of Smith-Waterman
