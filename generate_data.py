import pandas as pd
import numpy as np

np.random.seed(42)
n = 600

df = pd.DataFrame({
    'order_id': range(1, n+1),
    'date': pd.date_range('2024-01-01', periods=n, freq='D'),
    'city': np.random.choice(['Москва', 'Казань', 'Сочи', 'Омск', 'Тверь'], n),
    'product': np.random.choice(['хлеб', 'молоко', 'сыр', 'колбаса', 'масло'], n),
    'price': np.random.uniform(30, 800, n).round(2),
    'quantity': np.random.randint(1, 10, n),
    'customer_age': np.random.randint(18, 80, n),
    'rating': np.random.choice([1, 2, 3, 4, 5, np.nan], n),
    'discount': np.random.choice([0, 5, 10, 15, np.nan], n),
})

df.loc[10:15, 'customer_age'] = -5
df.loc[20, 'price'] = 999999
df.loc[30:35, 'city'] = '  москва '
df = pd.concat([df, df.iloc[:5]], ignore_index=True)

df.to_csv('data/dataset.csv', index=False)
print('Готово:', df.shape)