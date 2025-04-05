import random

# ✅ Dictionary of predefined medical conditions and responses
medical_responses = {
    "fever": "A fever is a temporary increase in body temperature. Stay hydrated and rest. If above 102°F, consult a doctor.",
    "cough": "A cough can be caused by infections, allergies, or irritants. Drink warm fluids and rest. If persistent, see a doctor.",
    "headache": "Headaches may be caused by stress, dehydration, or migraines. Drink water, rest, and avoid screen time.",
    "cold": "The common cold is a viral infection. Rest, drink warm fluids, and take vitamin C.",
    "flu": "Flu symptoms include fever, chills, and muscle pain. Stay hydrated and consider seeing a doctor if severe.",
    "diabetes": "Diabetes affects blood sugar levels. Maintain a balanced diet, exercise, and follow medical advice.",
    "hypertension": "High blood pressure can lead to heart issues. Reduce salt intake, exercise, and monitor blood pressure regularly.",
    "asthma": "Asthma causes breathing difficulties. Use an inhaler if prescribed and avoid triggers like dust and smoke.",
    "heart attack": "A heart attack causes chest pain and shortness of breath. Seek emergency medical attention immediately.",
    "stroke": "A stroke is a medical emergency. Symptoms include facial drooping and weakness in one side of the body. Call 911 immediately.",
    "migraine": "Migraines cause severe headaches and sensitivity to light. Rest in a dark room and avoid triggers.",
    "food poisoning": "Symptoms include vomiting and diarrhea. Drink plenty of fluids and rest. Seek medical help if severe.",
    "toothache": "Tooth pain can be caused by cavities. Rinse with salt water and see a dentist if pain persists.",
    "kidney stones": "Kidney stones cause severe pain. Drink lots of water and seek medical advice.",
    "UTI": "Urinary tract infections cause burning urination. Drink cranberry juice and see a doctor if symptoms persist.",
    "liver disease": "Liver issues can cause jaundice and fatigue. Avoid alcohol and consult a specialist.",
    "thyroid disorder": "Thyroid imbalance can cause weight changes. Get thyroid levels checked by a doctor.",
    "cancer": "Cancer treatment depends on type and stage. Consult an oncologist for proper management.",
    "HIV": "HIV weakens immunity. Take antiretroviral medication and maintain a healthy lifestyle.",
    "COVID-19": "COVID-19 symptoms include fever, cough, and loss of smell. Isolate and seek medical attention if breathing is difficult.",
}

# Default fallback responses
default_responses = [
    "I'm not sure about that. Can you provide more details?",
    "I can help with medical questions like fever, cough, or headache. What are your symptoms?",
    "I'm here to provide basic health advice. If it's serious, please consult a doctor."
]

def get_response(user_message):
    """
    Checks if user input matches a predefined medical condition and returns a response.
    """
    user_message = user_message.lower().strip()  # Normalize input

    for condition in medical_responses.keys():
        if condition in user_message:
            return medical_responses[condition]  # ✅ Return predefined response

    return random.choice(default_responses)  # ✅ Return fallback response if no match is found
