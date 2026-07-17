from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.DataFrame({
    "interaction_count":[0,1,2,3,4],
    "medicine_count":[1,2,4,5,6],
    "trusted_source":[1,1,1,0,0],
    "high_confidence_extraction":[1,1,0,0,0],
    "risk":[0,0,1,1,1]
})

X = data.drop("risk", axis=1)
y = data["risk"]

model = RandomForestClassifier()
model.fit(X,y)