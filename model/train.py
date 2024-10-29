# train.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import pathlib
from joblib import dump

# Cargar el dataset
df = pd.read_csv('./data/mountains_vs_beaches_preferences.csv')

# Preparar los datos
X = df.drop('Preference', axis=1)  # 'Preference' es la columna objetivo
y = df['Preference']

# Convertir variables categóricas a variables dummy
X = pd.get_dummies(X, drop_first=True)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo
dump(model, './model/mountains_vs_beaches-v1.joblib')

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')
print(classification_report(y_test, y_pred))
