# 🍽️ Food Demand Predictor Using AI

A smart AI-powered system that predicts the number of vegetarian and non-vegetarian meals to prepare in a canteen based on student attendance. Built using **LangGraph**, **Streamlit**, and **Python**.

## Objective
Reduce food waste by predicting exact food demand based on:
- Number of registered and present students
- Special event information
- Veg/non-veg preference

## Inputs
- Number of students registered
- Number of students present
- Is there a special event? (yes/no)
- Vegetarian ratio (%)

## Output
- Total meals (with buffer)
- Split of vegetarian and non-vegetarian meals
- Explanation in English, Hindi, and Gujarati
- Downloadable daily report (.csv)

---

## ⚙️ Workflow

### Step-by-step process:

1. **User Input**
   - Streamlit UI collects data: students registered, present, event status, veg %

2. **LangGraph Agent Starts**
   - LangGraph manages state transitions (input → process → output)

3. **AI Prediction Logic**
   - `predict_meals.py`:
     - Calculates total meals: `present + buffer`
     - Splits veg vs non-veg using ratio
     - Generates human-like explanation

4. **Multilingual Explanation**
   - Explanation is translated to **Hindi** and **Gujarati**

5. **Daily CSV Logging**
   - Each prediction is saved in `daily_report.csv` with date & details

6. **User Downloads Report**
   - Streamlit displays output with button to download report
---

## Features
- AI-based logic for food prediction
- Multilingual output (EN | HI | GU)
- QR code login simulation for mess manager
- Daily trend CSV logging

---

---

> ## Developed as part of the UN SDG Goal #2: Zero Hunger initiative.
