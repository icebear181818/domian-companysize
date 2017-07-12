import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import accuracy_score
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import statsmodels.formula.api as smf
import matplotlib as plt


#training the input data
data=pd.read_csv('C:\Users\jessica_zhu1\Desktop\pyproj\output\company',sep="\t", header=None, names=["alexa", "em"])
data1=pd.read_csv('C:\Users\jessica_zhu1\Desktop\pyproj\output\company1',sep="\t", header=None, names=["talexa", "em"])
lm1=smf.ols(formula='em ~ alexa',data=data).fit()
print lm1.summary()

#prediction
a=pd.DataFrame()
a['alexa']=data1['talexa']
a['em']=lm1.predict(a)


#fitting curve
sns.lmplot(data=data, x='alexa', y='em', line_kws={'color': 'red'})
plt.title('Alexa and Employee Number(260 Records)')
plt.show()


# calculate the accuracy
def bucket(c):
    if c['em']<=200:
        return 1
    if c['em']>200 and c['em']<=1000:
        return 2
    if c['em']<=3000 and c['em']>1000:
        return 3
    else:
        return 4
a['bucket']=a.apply(bucket, axis=1)
data1['bucket']=data1.apply(bucket, axis=1)
accracy=accuracy_score(data1['bucket'],a['bucket'],normalize=False)

print accracy


