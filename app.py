import streamlit as st
import pandas as pd
import joblib

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ==================================
# LOAD MODEL
# ==================================

model = joblib.load("fraud_pipeline .pkl")

# ==================================
# SESSION STATE
# ==================================

if "predict_page" not in st.session_state:
    st.session_state.predict_page = False

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("💳 Fraud Detection")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "ℹ About"
        ]
    )

# ==================================
# HOME PAGE
# ==================================

if page == "🏠 Home":

    if not st.session_state.predict_page:

        st.title("💳 Credit Card Fraud Detection")

        st.markdown("---")

        st.markdown("""
        ## Credit/Debit Card Fraud Detection System

        Detect suspicious credit card transactions
        using Machine Learning and receive instant
        fraud risk analysis.
        """)

        st.success(
            "Secure your transactions with real-time fraud prediction."
        )

        st.markdown("---")

        if st.button(
            "🚀 Start Prediction",
            use_container_width=True
        ):
            st.session_state.predict_page = True
            st.rerun()

    else:

        st.title("🔍 Fraud Prediction")

        if st.button("⬅ Back to Home"):
            st.session_state.predict_page = False
            st.rerun()

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            amt = st.number_input(
                "Transaction Amount",
                min_value=0.0,
                value=1000.0
            )

            category = st.text_input(
                "Category",
                "shopping"
            )

            city = st.text_input(
                "City",
                "Bhubaneswar"
            )

            state = st.text_input(
                "State",
                "Odisha"
            )

        with col2:

            job = st.text_input(
                "Job",
                "Student"
            )

            city_pop = st.number_input(
                "City Population",
                min_value=0,
                value=100000
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=21
            )

            transaction_time = st.time_input(
                "Transaction Time"
            )

        st.markdown("---")

        if st.button(
            "🚀 Analyze Transaction",
            use_container_width=True
        ):

            hour = transaction_time.hour

            sample = pd.DataFrame([{
                "amt": amt,
                "category": category,
                "city": city,
                "state": state,
                "job": job,
                "city_pop": city_pop,
                "hour": hour,
                "day": 15,
                "month": 6,
                "dayofweek": 0,
                "age": age
            }])

            prediction = model.predict(sample)[0]

            probability = model.predict_proba(sample)[0][1]

            risk = probability * 100

            st.markdown("---")

            st.subheader("📊 Prediction Result")

            if prediction == 1:

                st.error(
                    "⚠ Fraudulent Transaction Detected"
                )

            else:

                st.success(
                    "✅ Legitimate Transaction"
                )

            st.metric(
                "Fraud Risk Score",
                f"{risk:.2f}%"
            )

            st.progress(int(risk))

            # ==========================
            # RISK ANALYSIS
            # ==========================

            if risk < 30:

                st.success(
                    "🟢 Low Risk"
                )

            elif risk < 60:

                st.warning(
                    "🟡 Medium Risk"
                )

                st.info("""
Monitor this transaction carefully.

If you do not recognize it,
contact your bank immediately.
""")

            else:

                st.error(
                    "🔴 High Risk"
                )

                st.warning("""
Recommended Actions

• Block or freeze your card immediately
• Contact your bank's fraud department
• Change your banking password
• Enable two-factor authentication
• Monitor recent transactions
""")

                st.subheader(
                    "🚨 Cyber Crime Support"
                )

                st.info("""
Cyber Crime Helpline (India)

📞 1930

🌐 https://cybercrime.gov.in

Report suspicious online fraud immediately.
""")

            with st.expander(
                "📄 Transaction Details"
            ):
                st.dataframe(
                    sample,
                    use_container_width=True
                )

# ==================================
# ABOUT PAGE
# ==================================

elif page == "ℹ About":

    st.title("ℹ About Project")

    st.markdown("---")

    st.write("""
### Credit Card Fraud Detection System

This project uses Machine Learning
to identify potentially fraudulent
credit card transactions.

### Technologies Used

• Python

• Pandas

• Scikit-Learn

• Random Forest

• One-Hot Encoding

• Streamlit

### Objective

To detect fraudulent credit card
transactions and provide risk analysis
for users.

### Workflow

Upload Dataset

↓

Dataset Overview

↓

EDA Dashboard

↓

Data Preprocessing

↓

Model Training

↓

Accuracy & Metrics

↓

Fraud Prediction

↓

Risk Score Dashboard
""")