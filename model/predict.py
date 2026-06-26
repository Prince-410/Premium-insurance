import pickle
import pandas as pd

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    prediction = model.predict(df)[0]
    
    probabilities = model.predict_proba(df)[0]    
    confidence_scores = {class_labels[i]: probabilities[i] for i in range(len(class_labels))}

    return {
        'insurance_premium_category': prediction,
        'confidence_scores': confidence_scores 
    }