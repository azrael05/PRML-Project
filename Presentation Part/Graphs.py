import plotly as plt
import pandas as pd
import matplotlib.pyplot as plt
# Read the data
x=[1,2,3]
y=[1,2,3]
# plt.plot(x,y)
# plt.show()
import plotly.express as px

# fig=px.bar(x=[1,2,3],y=[1,2,3])
# fig.show()
df=pd.read_excel(r"D:\PRML\Presentation Part\accuracy_score-SVM.xlsx")
x=df['Features']
y=df['Ramdom Forest','SVM - POLY','SVM- Linear']
print(y)