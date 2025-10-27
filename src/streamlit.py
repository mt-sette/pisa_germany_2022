import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="PISA 2022 Germany Analysis", page_icon="📊", layout="wide"
)

# Header
st.title("PISA 2022 Germany Analysis")
st.markdown(
    "**Research Question:** Do migrant children perform worse due to language barriers or low socioeconomic status?"
)
st.markdown("**Sample:** 5,046 students | **Data:** PISA 2022 Germany")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox(
    "Select Section:", ["Overview", "Key Findings", "Analysis", "Conclusions"]
)

if section == "Overview":
    st.header("📊 Overview")

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Sample", "5,046")
    with col2:
        st.metric("German Speakers", "82.4%")
    with col3:
        st.metric("Reading Gap", "85.5 pts")
    with col4:
        st.metric("SES Effect", "+34 pts")

    st.markdown("""
    **Methodology:** Sequential regression modeling to decompose variance explained by:
    - Socioeconomic Status (SES) 
    - Language at Home (German vs Other)
    - Migration Status
    """)

elif section == "Key Findings":
    st.header("🔍 Key Findings")

    # Achievement gaps
    st.subheader("Raw Achievement Gaps")
    scores_data = pd.DataFrame(
        {
            "Subject": ["Mathematics", "Reading", "Science"],
            "German Speakers": [500.0, 506.1, 520.7],
            "Other Language": [427.6, 420.6, 433.0],
            "Gap (points)": [72.4, 85.5, 87.7],
        }
    )
    st.dataframe(scores_data, use_container_width=True)

    # Variance explained
    st.subheader("Variance Explained (R²)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("SES alone", "13.5%")
    with col2:
        st.metric("Language alone", "7.2%")
    with col3:
        st.metric("Language beyond SES", "3.7%")

    # Key insight
    st.info(
        "**Key Insight:** Students speaking other languages have significantly lower SES (-0.641 vs +0.040), but language barriers still have an independent effect."
    )

elif section == "Analysis":
    st.header("📈 Analysis")

    # SES x Language interaction analysis
    st.subheader("SES x Language Interaction")

    try:
        st.image(
            "src/img/ses_language_interaction.png",
            caption="Interaction of SES and Language on Achievement",
            use_container_width=False,
            #width=800,  # Adjust as needed for your preferred size
        )
    except FileNotFoundError:
        st.warning("SES x Language interaction plot not found")
    except Exception as e:
        st.warning(f"Error loading SES x Language interaction plot: {e}")

    # Regression results with interaction term
    st.subheader("Regression Results with SES x Language Interaction")
    interaction_results = pd.DataFrame(
        {
            "Model": [
                "SES only",
                "Language only",
                "SES + Language",
                "SES + Language + SES x Language"
            ],
            "R²": [0.135, 0.072, 0.172, 0.178],
            "MAE": [79.5, 82.6, 77.5, 76.9],
        }
    )
    st.dataframe(interaction_results, use_container_width=True)

    # Coefficients
    st.subheader("Key Coefficients (SES + Language Model)")
    coef_data = pd.DataFrame(
        {
            "Variable": ["SES (per SD)", "Language (German vs Other)"],
            "Coefficient": [34.0, -64.1],
            "Interpretation": [
                "Points per SD increase in SES",
                "Points difference (German speakers higher)",
            ],
        }
    )
    st.dataframe(coef_data, use_container_width=True)

    # Subject-specific analysis
    try:
        st.image(
            "src/img/subject_comparison.png",
            caption="Subject-Specific Analysis",
            use_container_width=True,
        )
    except FileNotFoundError:
        st.warning("Subject comparison plot not found")
    except Exception as e:
        st.warning(f"Error loading subject comparison plot: {e}")
        
    # Residual Analysis
    st.subheader("Residual Analysis")
    try:
        st.image(
            "src/img/residual_analysis.png",
            caption="Residuals after Controlling for SES",
            use_container_width=True,
        )
    except FileNotFoundError:
        st.warning("Residual analysis plot not found")
    except Exception as e:
        st.warning(f"Error loading residual analysis plot: {e}")
        
    st.subheader("Residuals: Mean Residuals by Language Group")
    residuals_summary = pd.DataFrame(
        {
            "mean": [10.25, -48.13],
            "std": [94.55, 104.48],
            "count": [4160, 886],
        },
        index=["German", "Other Language"],
    )
    st.dataframe(residuals_summary, use_container_width=True)

    # Summary metrics and interpretation
    mean_diff = 58.38
    st.metric("Mean difference (German − Other)", f"{mean_diff:.2f} pts")
    st.markdown("**Interpretation:** After controlling for SES, language minorities score 58.4 points lower.")

    # T-test reporting
    t_stat = 16.374
    p_val = 0.0
    st.markdown(f"**T-test:** t = {t_stat:.3f}, p = {p_val:.4f}")
    st.success("*** Highly significant difference (p < 0.001) ***")

elif section == "Conclusions":
    st.header("💡 Conclusions")

    # Final answer
    st.success(
        "**Answer:** Both SES and language matter, but SES is ~2x more important. However, language barriers have a meaningful INDEPENDENT effect."
    )

    # Key findings summary
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Primary Driver:**
        - SES explains 13.5% of variance
        - 1 SD increase in SES → +34 points
        - Students with language barriers have lower SES
        """)

    with col2:
        st.markdown("""
        **Secondary Factor:**
        - Language explains 7.2% of variance
        - Language adds 3.7% beyond SES
        - 58.4 point gap persists after controlling for SES
        """)

    # Policy implications
    st.subheader("Policy Implications")
    st.markdown("""
    1. **Address socioeconomic inequality** as primary intervention
    2. **Provide targeted language support** for non-German speakers  
    3. **Implement early intervention** programs addressing both factors
    4. **Consider compounding effects** of multiple disadvantages
    """)

    # Technical details
    with st.expander("Technical Details"):
        st.markdown("""
        - **Data:** PISA 2022 Germany (5,046 students)
        - **Method:** Sequential regression modeling
        - **Significance:** p < 0.001 for all key findings
        - **Software:** Python (pandas, scikit-learn, scipy)
        """)

# Footer
st.markdown("---")
st.markdown("*Data Science WBS Capstone Project*")
