import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# --- STEP 1: LOAD & TRAIN (The "Brain") ---
@st.cache_resource # This keeps the model in memory so it's fast
def load_and_train():
    df = pd.read_csv('cleaned_ecommerce_data.csv')
    features = ['age', 'time_on_site', 'pages_viewed', 'previous_purchases', 
                'cart_items', 'ad_clicked', 'returning_user', 
                'avg_session_time', 'bounce_rate']
    X = df[features]
    y = df['hesitant_users']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = load_and_train()

# --- STEP 2: USER INTERFACE ---
st.set_page_config(page_title="AI Hesitation Detector", layout="wide")
st.title("🛒 Real-Time Hesitation Detector")
st.markdown("This AI monitors user behavior and triggers a 'Smart Alert' before they abandon their cart.")

# Sidebar for Simulation
st.sidebar.header("Simulate User Behavior")
age = st.sidebar.slider("User Age", 18, 80, 30)
time_on_site = st.sidebar.slider("Time on Site (Minutes)", 1, 30, 5)
pages_viewed = st.sidebar.slider("Pages Viewed", 1, 20, 3)
prev_purchases = st.sidebar.number_input("Previous Purchases", 0, 50, 2)
cart_items = st.sidebar.number_input("Items currently in Cart", 0, 10, 1)
returning = st.sidebar.selectbox("Is Returning User?", [0, 1])
bounce = st.sidebar.slider("Bounce Rate %", 0, 100, 20)

# Create input for model
input_data = pd.DataFrame([[age, time_on_site, pages_viewed, prev_purchases, 
                            cart_items, 0, returning, 15, bounce]], 
                          columns=['age', 'time_on_site', 'pages_viewed', 'previous_purchases', 
                                   'cart_items', 'ad_clicked', 'returning_user', 
                                   'avg_session_time', 'bounce_rate'])

# --- STEP 3: PREDICTION ---
prediction_prob = model.predict_proba(input_data)[0][1] # Get probability of hesitation
hesitant_users = model.predict(input_data)[0]


# --- STEP 4: DISPLAY RESULTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("AI Analysis")
    st.metric(label="Hesitation Probability", value=f"{prediction_prob*100:.1f}%")
    
    # CHANGE THIS LINE BELOW:
    if hesitant_users: 
        st.error("⚠️ AI STATUS: HESITATION DETECTED")
    else:
        st.success("✅ AI STATUS: NORMAL BROWSING")

with col2:
    st.subheader("AI Smart Alert: Popularity & Value")
    # CHANGE THIS LINE BELOW AS WELL:
    if hesitant_users:
        st.info("💡 **AI Recommendation:** Show the Popularity Alert + Price Incentive")
        st.toast("High Demand! 50 other people bought this today.")
        st.warning("### Don't Miss Out!")
        st.write("This Tablet is trending right now. Use your active **10% discount** before stock runs out!")
        st.image("tablet.jpeg", width=300)
        st.write("Customers who viewed this also liked: [Mobile]")
    else:
        st.write("No smart alert needed. Monitoring activity...")
