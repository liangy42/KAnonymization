from Anonymization_MainAlgo import AnonymizeByLpGurobiMain
from Anonymization_Greedy_YMILP import AnonymizeByGreedyYMILP

strFile = '../../example/person20_4attr.csv'
strFileAtt = '../../example/person_4att_sup.txt'
strFileOut = '../../example/person20_4attr_k3s3.csv'
AnonymizeByLpGurobiMain(strFile,strFileAtt,3,3, strFileOut)




# AnonymizeByGreedyYMILP('../../example/1k_8attr.txt','../../example/doka_attr_numerical.txt',3, '../../1k8attr_GreedyYMILP_k3.csv')