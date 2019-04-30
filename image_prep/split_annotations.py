#%%
import numpy as np
import pandas as pd

#%%
full_labels = pd.read_csv("april_annotations.csv")
grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()


#%%
gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]
len(grouped_list)

#%%
train_index = np.random.choice(len(grouped_list), size=(int(len(grouped_list)*.8)), replace=False)
test_index = np.setdiff1d(list(range(len(grouped_list))), train_index)
len(train_index), len(test_index)

# take # files files
train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])

#%%
len(train), len(test)
train.to_csv('train_labels.csv', index=None)
test.to_csv('test_labels.csv', index=None)