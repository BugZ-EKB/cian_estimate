import pandas as pd
import pickle 
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score

fields = [
            'link', 'floor', 'floors_count', 'rooms_count',
            'total_meters',	'price', 'year_of_construction',
            'living_meters',	'kitchen_meters',	'district'
        ]


df = pd.read_csv(
    "cian_parsing_full.csv",
    sep=';'
)
#print(df)

del df['link']
del df['author']
del df['street']
del df['city']
del df['accommodation_type']
del df['deal_type']
del df['phone']
del df['residential_complex']
del df['underground']


print(df)
encoder = LabelEncoder()
encoder.fit(df['district'])
df['district'] = encoder.transform(df['district'])

y, X = df['price'], df.drop('price', axis=1)

cat = CatBoostRegressor()
cat.fit(X, y)
y_cat_pred = cat.predict(X)

print(r2_score(y, y_cat_pred))

filename = 'finalized_model.pql'
pickle.dump(cat, open(filename, 'wb'))