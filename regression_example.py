import pandas as pd
import pickle 
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score
import numpy as np
from sklearn.model_selection import train_test_split


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

encoder = LabelEncoder()
encoder.fit(df['district'])
df['district'] = encoder.transform(df['district'])

y, X = df['price'], df.drop('price', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

cat = CatBoostRegressor()
cat.fit(X_train, y_train)
y_cat_pred = cat.predict(X_test)

print(r2_score(y_test, y_cat_pred))

filename = 'finalized_model.pkl'
pickle.dump(cat, open(filename, 'wb'))