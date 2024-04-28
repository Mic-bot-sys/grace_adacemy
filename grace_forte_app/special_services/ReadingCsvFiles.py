import pandas as pd
import uuid

data = pd.read_csv('school_test.csv')

for index, d in data.iterrows():
    print('================================')
    data.at[index, 'id'] = uuid.uuid4()
print(data)