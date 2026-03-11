import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

classes = ['apple','cucumber','banana','strawberry','pomegranate',
           'muffin','tea','mango','pear','cookie','lemon','avocado']

precision = [40,50,75,40,100,60,58,100,100,34,34,50]
recall    = [67,100,100,100,100,100,100,100,33,100,100,100]
f1_score  = [50,67,86,57,100,75,73,100,50,50,50,67]

data = pd.DataFrame({
    'Precision': precision,
    'Recall': recall,
    'F1-score': f1_score
}, index=classes)

plt.figure(figsize=(10,6))
sns.heatmap(data, annot=True, fmt=".0f", cmap='YlGnBu')  
# fmt=".0f" → show integers without scientific notation

plt.title("Model Performance Heatmap")
plt.ylabel("Classes")
plt.show()

