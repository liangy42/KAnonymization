from Anonymization_MainAlgo import AnonymizeByLpGurobiMain
from Anonymization_Greedy_YMILP import AnonymizeByGreedyYMILP
from Anonymization_Greedy_kmember import AnonymizeByGreedyKMember


AnonymizeByLpGurobiMain('CENSUS/20k_4attr.txt','CENSUS/census_20k4attr_sup_noweight.txt',3,3,'results/census_20K4attr_k3_w0wvar.csv')
# AnonymizeByLpGurobiMain('CENSUS/20k_4attr.txt','CENSUS/census_20k4attr_sup_noweight.txt',5,3,'results/census_20K4attr_k5_w0wvar.csv')
# AnonymizeByGreedyKMember('CENSUS/20k_4attr.txt','example/doka_attr_numerical.txt',3,'results/census_20K4attr_kmember_k3.csv')
# AnonymizeByGreedyKMember('CENSUS/20k_4attr.txt','example/doka_attr_numerical.txt',5,'results/census_20K4attr_kmember_k5.csv')
