from langgraphagent.state.state import FoodDemandState
from langgraphagent.LLMS.load_model import load_llm
from langchain_core.messages import HumanMessage

def predict_meals(state: FoodDemandState) -> FoodDemandState:
    buffer = 2  # extra meals buffer
    total_meals = state['present'] + buffer

    veg_percent = state.get('veg_ratio', 70)
    veg_count = int((veg_percent / 100) * total_meals)
    non_veg_count = total_meals - veg_count

    eng_output = (
        f"A simple problem!\n\n"
        f"Since {state['present']} students are present, and {state['registered']} are registered, "
        f"that means {state['registered'] - state['present']} students are absent.\n"
        f"To avoid waste, the mess should prepare meals for the {state['present']} present students, "
        f"plus a buffer of {buffer} extra meals.\n\n"
        f" Total meals to prepare: {total_meals}\n"
        f"🥗 Vegetarian meals: {veg_count}\n"
        f"🍗 Non-Vegetarian meals: {non_veg_count}\n"
    )

    hindi_output = (
        f"\n\n**हिंदी में अनुवाद:**\n"
        f"कुल {state['present']} छात्र उपस्थित हैं और {state['registered']} पंजीकृत हैं, तो {state['registered'] - state['present']} अनुपस्थित हैं।\n"
        f"भोजन की बर्बादी रोकने के लिए, मेस को {buffer} अतिरिक्त भोजन के साथ {state['present']} छात्रों के लिए भोजन बनाना चाहिए।\n"
        f"कुल भोजन: {total_meals}, शाकाहारी: {veg_count}, मांसाहारी: {non_veg_count}"
    )

    gujarati_output = (
        f"\n\n**ગુજરાતીમાં અનુવાદ:**\n"
        f"કુલ {state['present']} વિદ્યાર્થીઓ હાજર છે અને {state['registered']} નોંધાયેલા છે, તો {state['registered'] - state['present']} ગેરહાજર છે.\n"
        f"ભોજન બગાડથી બચવા માટે, મેષે {buffer} વધારાના ભોજન સાથે {state['present']} વિદ્યાર્થીઓ માટે ભોજન તૈયાર કરવું જોઈએ.\n"
        f"કુલ ભોજન: {total_meals}, શાકાહારી: {veg_count}, માંસાહારી: {non_veg_count}"
    )

    state["ai_response"] = eng_output + hindi_output + gujarati_output
    return state

