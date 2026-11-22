import sys

import joblib
import pandas as pd


saved = joblib.load("model.joblib")
data = pd.read_csv(sys.argv[1])
probability = saved["model"].predict_proba(data)[:, 1]
result = pd.DataFrame({
    "cancellation_probability": probability.round(4),
    "is_canceled": (probability >= saved["threshold"]).astype(int)
})
print(result.to_csv(index=False), end="")
