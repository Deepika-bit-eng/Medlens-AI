import streamlit as st
import requests
import tempfile

st.set_page_config(
    page_title="MedLens AI",
    page_icon="💊",
    layout="wide"
)

st.sidebar.title("💊 MedLens AI")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📄 Dashboard", "ℹ About"]
)

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.title("💊 MedLens AI")
    st.subheader("Understand your prescription. Don't just read it.")

    uploaded_file = st.file_uploader(
        "Upload Prescription",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        st.image(uploaded_file, use_container_width=True)

        if st.button("🔍 Analyze Prescription"):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                tmp.write(uploaded_file.read())
                image_path = tmp.name

            with st.spinner("Analyzing Prescription..."):

                files = {
                    "file": open(image_path, "rb")
                }

                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    files=files
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Complete!")

                st.subheader("Patient")

                st.write("**Name:**", result["patient_name"])
                st.write("**Doctor:**", result["doctor_name"])

                st.divider()

                st.subheader("Medicines")

                for medicine in result["medicines"]:

                    with st.expander(medicine["name"]):

                        st.write("### Purpose")
                        st.write(medicine["purpose"])

                        st.write("### Why Prescribed")
                        st.write(medicine["why_prescribed"])

                        st.write("### Side Effects")
                        st.write(medicine["common_side_effects"])

                        st.write("### Source")
                        st.success(medicine["source"])

                        st.write("### Trust Score")
                        st.progress(medicine["trust_score"] / 100)
                        st.write(f"{medicine['trust_score']}%")

                st.divider()

                st.subheader("Drug Interaction Report")

                report = result["interaction_report"]

                st.write("**Risk:**", report["risk"])
                st.write(report["summary"])

            else:
                st.error("Backend Error")

# ---------------- DASHBOARD ----------------

elif page == "📄 Dashboard":

    st.title("Dashboard")

    st.info("After analysis, medicine details will appear here.")

# ---------------- ABOUT ----------------

elif page == "ℹ About":

    st.title("About MedLens AI")

    st.write("""
MedLens AI helps users understand prescriptions using Explainable AI.

✔ OCR Prescription Reading

✔ Medicine Explanation

✔ Drug Interaction Detection

✔ Trust Score

✔ Reliable Medical Sources

Educational purposes only.
""")