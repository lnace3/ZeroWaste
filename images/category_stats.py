#%%
import glob
import pandas as pd
df = pd.concat([pd.read_csv(f) for f in glob.glob('.//labels_archive//*.csv')])

%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
class_count = df['class'].value_counts()
sns.set(style='darkgrid')
sns.barplot(class_count.index, class_count.values, alpha=0.9)
plt.title("Frequency Distribution of Categories")
plt.ylabel("Number of Occurances", fontsize = 12)
plt.xlabel('Item Classes', fontzie=12)
plt.show()
