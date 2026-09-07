import streamlit as st
import joblib
import pandas as pd
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
# =========================
# Load Model
# =========================

model = joblib.load("tuned_gradient_boosting_model.pkl")
feature_names = joblib.load("feature_names.pkl")


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)


# =========================
# Header
# =========================

st.title("⚙️ AI-Powered Predictive Maintenance")
st.markdown(
    "### Machine Failure Risk Analytics"
)

st.write(
    "Enter the machine parameters below to evaluate the probability "
    "of machine failure using a trained Gradient Boosting model."
)

st.divider()


# =========================
# Sidebar - Input Parameters
# =========================

st.sidebar.header("⚙️ Machine Parameters")

air_temp = st.sidebar.number_input(
    "Air Temperature [K]",
    min_value=250.0,
    max_value=350.0,
    value=300.0,
    step=0.1
)

process_temp = st.sidebar.number_input(
    "Process Temperature [K]",
    min_value=250.0,
    max_value=350.0,
    value=310.0,
    step=0.1
)

rpm = st.sidebar.number_input(
    "Rotational Speed [rpm]",
    min_value=500,
    max_value=3000,
    value=1500,
    step=10
)

torque = st.sidebar.number_input(
    "Torque [Nm]",
    min_value=0.0,
    max_value=100.0,
    value=40.0,
    step=0.5
)

tool_wear = st.sidebar.number_input(
    "Tool Wear [min]",
    min_value=0,
    max_value=300,
    value=100,
    step=1
)

machine_type = st.sidebar.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)


# =========================
# Prediction
# =========================

if st.button("🔍 Analyze Machine Risk", use_container_width=True):

    with st.spinner("🤖 Analyzing machine parameters..."):

        # Encode machine type
        type_L = 1 if machine_type == "L" else 0
        type_M = 1 if machine_type == "M" else 0

        # بقیه کدهای قبلی تحلیل و پیش‌بینی

    # Create input dataframe
    input_data = pd.DataFrame(
        [[
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear,
            type_L,
            type_M
        ]],
        columns=feature_names
    )

    # Model prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    probability_percent = probability * 100


    # =========================
    # Risk Level
    # =========================

    if probability_percent < 20:
        risk_level = "LOW"
        status_message = "🟢 Machine Operating Normally"

    elif probability_percent < 50:
        risk_level = "MEDIUM"
        status_message = "🟡 Moderate Failure Risk"

    else:
        risk_level = "HIGH"
        status_message = "🔴 High Failure Risk Detected"


    # =========================
    # Results
    # =========================

    st.subheader("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Failure Probability",
            f"{probability_percent:.2f}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk_level
        )

    with col3:
        st.metric(
            "Prediction",
            "Failure" if prediction == 1 else "No Failure"
        )


    st.divider()


    # =========================
    # Status
    # =========================

    if prediction == 1:
        st.error(status_message)
    else:
        if risk_level == "MEDIUM":
            st.warning(status_message)
        else:
            st.success(status_message)


    # =========================
    # Probability Bar
    # =========================

    st.write("### Failure Probability")

    st.progress(
        min(probability, 1.0)
    )


    # =========================
    # Machine Summary
    # =========================

    st.write("### 🔧 Machine Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Machine Type",
            "Air Temperature",
            "Process Temperature",
            "Rotational Speed",
            "Torque",
            "Tool Wear"
        ],
        "Value": [
            machine_type,
            f"{air_temp:.1f} K",
            f"{process_temp:.1f} K",
            f"{rpm} rpm",
            f"{torque:.1f} Nm",
            f"{tool_wear} min"
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )


    # =========================
    # Recommendation
    # =========================

    st.write("### 💡 Recommendation")

    if probability_percent < 20:

        st.info(
            "The machine currently shows a low predicted failure risk. "
            "Continue normal monitoring and maintenance."
        )

    elif probability_percent < 50:

        st.warning(
            "The machine shows a moderate failure risk. "
            "Consider closer monitoring and preventive maintenance."
        )

    else:

        st.error(
            "The machine shows a high predicted failure risk. "
            "Immediate inspection and preventive maintenance are recommended."
        )

# =========================
# Batch Prediction
# =========================

st.divider()

st.subheader("📁 Batch Machine Analysis")

st.write(
    "Upload a CSV or Excel file containing machine parameters "
    "to analyze multiple machines at once."
)

uploaded_file = st.file_uploader(
    "Upload machine data",
    type=["csv", "xlsx"],
    key="batch_machine_file"
)

if uploaded_file is not None:

    try:

        # =========================
        # Read Uploaded File
        # =========================

        if uploaded_file.name.endswith(".csv"):
            batch_data = pd.read_csv(uploaded_file)
        else:
            batch_data = pd.read_excel(uploaded_file)

        st.success(
            f"File uploaded successfully: {uploaded_file.name}"
        )

        st.write("### 📋 Uploaded Data")

        st.dataframe(
            batch_data,
            use_container_width=True,
            hide_index=True
        )

        # =========================
        # Required Columns
        # =========================

        required_columns = [
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]",
            "Type"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in batch_data.columns
        ]

        if missing_columns:

            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )

        else:

            # =========================
            # Encode Machine Type
            # =========================

            batch_data["Type_L"] = (
                batch_data["Type"] == "L"
            ).astype(int)

            batch_data["Type_M"] = (
                batch_data["Type"] == "M"
            ).astype(int)

            # =========================
            # Prepare Model Input
            # =========================

            batch_input = batch_data[feature_names]

            # =========================
            # Predictions
            # =========================

            batch_predictions = model.predict(
                batch_input
            )

            batch_probabilities = model.predict_proba(
                batch_input
            )[:, 1]

            # =========================
            # Add Results
            # =========================

            batch_data["Failure Probability"] = (
                batch_probabilities * 100
            ).round(2)

            batch_data["Prediction"] = batch_predictions

            batch_data["Prediction"] = batch_data[
                "Prediction"
            ].map({
                0: "No Failure",
                1: "Failure"
            })

            batch_data["Risk Level"] = batch_data[
                "Failure Probability"
            ].apply(
                lambda x:
                    "LOW" if x < 20
                    else "MEDIUM" if x < 50
                    else "HIGH"
            )

            # =========================
            # Summary
            # =========================

            st.write("### 📊 Batch Prediction Summary")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Total Machines",
                    len(batch_data)
                )

            with col2:

                st.metric(
                    "Predicted Failures",
                    int((batch_predictions == 1).sum())
                )

            with col3:

                st.metric(
                    "High Risk Machines",
                    int(
                        (
                            batch_data["Risk Level"]
                            == "HIGH"
                        ).sum()
                    )
                )

            # =========================
            # Results Table
            # =========================

            st.write("### 🔍 Detailed Results")

            result_columns = [
                "Type",
                "Air temperature [K]",
                "Process temperature [K]",
                "Rotational speed [rpm]",
                "Torque [Nm]",
                "Tool wear [min]",
                "Failure Probability",
                "Risk Level",
                "Prediction"
            ]

            st.dataframe(
                batch_data[result_columns],
                use_container_width=True,
                hide_index=True
            )

            # =========================
            # Download Results
            # =========================

            csv_result = batch_data.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="⬇️ Download Prediction Results",
                data=csv_result,
                file_name="machine_failure_predictions.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error(
            f"Error while processing the file: {e}"
        )


    # -------------------------
    # Risk Distribution
    # -------------------------
    st.subheader("⚠️ Risk Level Distribution")

    risk_counts = results["Risk Level"].value_counts()

    fig1, ax1 = plt.subplots()

    ax1.bar(
        risk_counts.index,
        risk_counts.values
    )

    ax1.set_xlabel("Risk Level")
    ax1.set_ylabel("Number of Machines")
    ax1.set_title("Machine Risk Distribution")

    st.pyplot(fig1)

    # -------------------------
    # Failure Probability
    # -------------------------
    st.subheader("📈 Failure Probability Distribution")

    fig2, ax2 = plt.subplots()

    ax2.hist(
        results["Failure Probability"],
        bins=10
    )

    ax2.set_xlabel("Failure Probability")
    ax2.set_ylabel("Number of Machines")
    ax2.set_title("Failure Probability Distribution")

    st.pyplot(fig2)

    # -------------------------
    # Prediction Distribution
    # -------------------------
    st.subheader("🔧 Machine Prediction")

    prediction_counts = results["Prediction"].map({
        0: "Normal",
        1: "Failure"
    }).value_counts()

    fig3, ax3 = plt.subplots()

    ax3.bar(
        prediction_counts.index,
        prediction_counts.values
    )

    ax3.set_xlabel("Prediction")
    ax3.set_ylabel("Number of Machines")
    ax3.set_title("Normal vs Failure Prediction")

    st.pyplot(fig3)

else:

    st.info(
        "Upload a batch file to display dashboard analytics."
    )
    # =========================
# Model Insights
# =========================

st.divider()

st.header("🧠 Model Insights")

# -------------------------
# Feature Importance
# -------------------------
st.subheader("🎯 Feature Importance")

if hasattr(model, "feature_importances_"):

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    }).sort_values(
        "Importance",
        ascending=True
    )

    fig4, ax4 = plt.subplots()

    ax4.barh(
        importance_df["Feature"],
        importance_df["Importance"]
    )

    ax4.set_xlabel("Importance")
    ax4.set_ylabel("Feature")
    ax4.set_title("Feature Importance - Gradient Boosting")

    st.pyplot(fig4)

    st.caption(
        "Higher importance indicates a stronger contribution "
        "to the model's prediction."
    )
    # -------------------------
# Model Performance
# -------------------------
st.subheader("🏆 Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Accuracy",
    "98.47%"
)

metric2.metric(
    "Precision",
    "88.29%"
)

metric3.metric(
    "Recall",
    "63.84%"
)

metric4.metric(
    "F1 Score",
    "73.97%"
)
# =========================
# Footer
# =========================

st.divider()

st.caption(
    "AI-Powered Predictive Maintenance | "
    "Gradient Boosting Model"
)
