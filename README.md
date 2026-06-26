# 🏥 Premium Insurance Prediction API

A FastAPI-based machine learning service that predicts the insurance premium category (`Low`, `Medium`, `High`) and computes confidence scores for each category based on user demographics, physical attributes, and lifestyle inputs.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Setup & Virtual Environment
Create and activate a virtual environment:
```bash
# Create the environment
python -m venv myenv

# Activate it (Windows)
myenv\Scripts\activate

# Activate it (macOS/Linux)
source myenv/bin/activate
```

### 3. Install Dependencies
Install the required packages:
```bash
pip install fastapi uvicorn pandas scikit-learn pydantic
```

### 4. Run the API
Start the FastAPI server using Uvicorn:
```bash
uvicorn app:app --reload
```
The server will start at `http://127.0.0.1:8000`.

---

## 🔌 API Endpoints

### 1. Home
* **URL**: `/`
* **Method**: `GET`
* **Description**: Welcome message.
* **Response**:
  ```json
  {
    "message": "Welcome to the Insurance Premium Prediction API!"
  }
  ```

### 2. Health Check
* **URL**: `/health`
* **Method**: `GET`
* **Description**: Check if the service is running and the ML model is successfully loaded.
* **Response**:
  ```json
  {
    "status": "healthy",
    "model_version": "1.0.0",
    "model_loaded": true
  }
  ```

### 3. Predict Premium Category
* **URL**: `/predict`
* **Method**: `POST`
* **Description**: Accepts user profile data, performs real-time feature engineering, and runs prediction.
* **Request Body**:
  ```json
  {
    "age": 35,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }
  ```
  * **Allowed Occupations**: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job`.
  
* **Response**:
  ```json
  {
    "response": {
      "insurance_premium_category": "Low",
      "confidence_scores": {
        "Low": 0.85,
        "Medium": 0.12,
        "High": 0.03
      }
    }
  }
  ```

---

## 🧠 Feature Transformations Under the Hood

The API automatically maps raw user inputs to engineered features expected by the machine learning model in [user_input.py](file:///d:/Premium-insurance/schema/user_input.py):
1. **BMI Calculation**: `weight / (height ^ 2)`
2. **Lifestyle Risk**: Categorized as `high` (smoker & BMI > 30), `medium` (smoker or BMI > 27), or `low` (others).
3. **Age Group**: Categorized as `young` (< 25), `adult` (< 45), `middle_aged` (< 60), or `senior` (≥ 60).
4. **City Tier**: Maps the input `city` to `1` (Tier 1 cities: Mumbai, Delhi, Bangalore, etc.), `2` (Tier 2 cities), or `3` (others).

---

## 📁 Project Structure

* [app.py](file:///d:/Premium-insurance/app.py): The main FastAPI application entry point.
* [schema/](file:///d:/Premium-insurance/schema/): Pydantic validation schemas.
  * [user_input.py](file:///d:/Premium-insurance/schema/user_input.py): Input data model and validation with custom computed fields.
  * [prediction_response.py](file:///d:/Premium-insurance/schema/prediction_response.py): Output response structure.
* [model/](file:///d:/Premium-insurance/model/): Serialization and inference code.
  * [predict.py](file:///d:/Premium-insurance/model/predict.py): Model loading and prediction logic.
  * `model.pkl`: The serialized pre-trained Scikit-Learn classification model.
* [config/](file:///d:/Premium-insurance/config/): Configuration modules.
  * [city_tier.py](file:///d:/Premium-insurance/config/city_tier.py): Listing of cities classified under Tier 1 and Tier 2.
* [insurance.csv](file:///d:/Premium-insurance/insurance.csv): The reference dataset containing user demographics and target premium categories.