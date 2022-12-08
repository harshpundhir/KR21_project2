from BayesNet import BayesNet
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
obj = BayesNet()
graph = obj.load_from_bifxml("/Users/harshpundhir/test/kr2proj/KR21_project2/testing/lecture_example.BIFXML")
nx.draw(obj.get_interaction_graph(), with_labels = True)
plt.savefig("filename.png")
x = obj.get_all_variables()
y = obj.get_all_cpts()
print(x[0])
#loooollll
print(y['Winter?'].iat[1,1])

