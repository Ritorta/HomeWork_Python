# Work №10 - Task №1
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()


# ------------
# Вариант №1
# ------------

# import random
# import pandas as pd
# from sklearn. preprocessing import OneHotEncoder

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# # print(data)

# encoder = OneHotEncoder(handle_unknown='ignore')
# encoder_df = pd.DataFrame(encoder. fit_transform(data[['whoAmI']]). toarray ())
# final_df = data.join (encoder_df)
# final_df.drop('whoAmI', axis= 1 , inplace= True )
# final_df.columns = ['human', 'robot']

# print(final_df)

# ------------
# Вариант №2
# ------------

import pandas as pd 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# print(data)

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
final_df = data.unstack(level=-1, fill_value = 0).astype(int)
final_df.columns = final_df.columns.droplevel()
final_df.columns.name = None
print(final_df)