# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df= pd.read_csv("Ecommerce Customers.csv")

# %%
from sklearn.model_selection import train_test_split
x=df[['Avg. Session Length', 'Time on App', 'Time on Website','Length of Membership']]
y=df[['Yearly Amount Spent']]

# %%
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

# %%
from sklearn.linear_model import LinearRegression

# %%
model=LinearRegression()

# %%
model.fit(X_train,y_train)


# %%
pred1=model.predict(X_test)
pred2=model.predict(X_train)

# %%
import pickle

# %%
with open("model.pkl","wb") as f:
    pickle.dump(model,f)



