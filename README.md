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

The API maps raw inputs to engineered features expected by the machine learning model:
1. **BMI Calculation**: `weight / (height ^ 2)`
2. **Lifestyle Risk**: Categorized as `high` (smoker & BMI > 30), `medium` (smoker or BMI > 27), or `low` (others).
3. **Age Group**: Categorized as `young` (< 25), `adult` (< 45), `middle_aged` (< 60), or `senior` (≥ 60).
4. **City Tier**: Maps `city` to `1` (Tier 1), `2` (Tier 2), or `3` (others).