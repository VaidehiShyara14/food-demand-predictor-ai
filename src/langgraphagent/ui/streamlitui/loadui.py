import streamlit as st
import pandas as pd
from datetime import datetime
from langgraphagent.state.state import FoodDemandState
from langgraphagent.nodes.predict_meals import predict_meals
from langgraphagent.ui.streamlitui.display_result import show_result
#from langgraphagent.ui.streamlitui.qr_auth import show_qr_login
import io

def launch_ui():
    st.title("🍽️ Food Demand Predictor")



    registered = st.number_input("Number of students registered:", min_value=0)
    present = st.number_input("Number of students present:", min_value=0)
    event = st.radio("Is there a special event today?", ["yes", "no"])
    veg_ratio = st.slider("Estimated % of Vegetarian Students:", 0, 100, 70)

    if st.button("Predict Meals"):
        state = FoodDemandState({
            "registered": registered,
            "present": present,
            "event": event,
            "veg_ratio": veg_ratio
        })
        updated_state = predict_meals(state)
        result_text = updated_state.get("ai_response", "No prediction returned.")
        show_result(result_text)

        # CSV export
        log_data = {
            "date": [datetime.now().strftime("%d-%b-%y")],
            "registered": [registered],
            "present": [present],
            "event": [event],
            "veg_ratio": [veg_ratio],
            "result": [result_text.replace("\n", " ")[:250]]
        }
        df = pd.DataFrame(log_data)
        with open("daily_report.csv", "a", encoding="utf-8", newline="") as f:
            df.to_csv(f, header=f.tell()==0, index=False)
        st.success(" Report saved to daily_report.csv")

        # Download button
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="⬇ Download Today's Report",
            data=csv_buffer.getvalue(),
            file_name="today_food_demand.csv",
            mime="text/csv"
        )