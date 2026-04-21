import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(
    page_title="Walmart Data Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Walmart Sales Data Chatbot")
st.markdown(
    "Ask me anything about the Walmart weekly sales dataset."
    " Powered by **Google Gemini API**."
)
st.divider()

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Enter your Gemini API Key",
        type = "password",
        placeholder = "Type of Gemini API Key..."
    )
    st.markdown("---")
    st.markdown("**About the App**")
    st.markdown(
        "This Chatbot uses Google Gemini API to answer"
        " questions about the Walmart Sales Dataset using"
        " prompt engineering and data summarisation."
    )
    st.markdown("Built by **Mohit Priya Ramtekkar**")
    st.markdown(
        "[GitHub](https://github.com/mohitramtekkar5-oss) | "
        "[LinkedIn](https://linkedin.com/in/mohit-priya-ramtekkar)"
    )

uploaded_file = st.file_uploader("Upload your Dataset", type=["csv"])

@st.cache_data
def load_and_summarize_data(file):
    df = pd.read_csv(file)
    summary_parts = []
    summary_parts.append(f"Dataset Shape: {df.shape[0]} rows and {df.shape[1]} columns")
    summary_parts.append(f"columns: {', '.join(df.columns.tolist())}")
    summary_parts.append("\nNumerical Summary:\n" + df.describe().round(2).to_string())
    if 'Holiday Flag' in df.columns:
        holiday = df.groupby('Holiday Flag')['Weekly_Sales'].agg(['mean','median','count']).round(2)
        holiday.index = ['Non-Holiday', 'Holiday']
        summary_parts.append("\nHoliday VS Non-Holiday Sales:\n" + holiday.to_string())
    if 'Store' in df.columns:
        top_stores = df.groupby('Store')['Weekly_Sales'].mean().round(2).nlargest(5)
        bottom_stores = df.groupby('Store')['Weekly_Sales'].mean().round(2).nsmallest(5)
        summary_parts.append("\nSample Data (First 5 Rows):\n" + df.head().to_string())
        summary_parts.append("\nTop 5 Stores by Average Sales:\n" + top_stores.to_string())
        summary_parts.append("\nBottom 5 Stores by Average Sales:\n" + bottom_stores.to_string())
    summary_parts.append("\nSample Data (First 5 Rows):\n" + df.head().to_string())
    return df, "\n".join(summary_parts)

def get_gemini_response(question, data_summary, api_key, chat_history):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    history_text = ""
    for msg in chat_history[-6:]:
        Role = "User" if msg["Role"] == "user" else "Assistant"
        history_text += f"{Role}: {msg['Content']}\n"
    prompt = f"""
You are a Senior Data Analyst specialising in retail sales analytics.
You have been given a summary of the Walmart Weekly Sales dataset.
Answer the user's question clearly, using specific numbers from the
data summary wherever possible. Keep answers concise but insightful.
If the question cannot be answered from the data, say so honestly.

--- DATASET SUMMARY ---
{data_summary}
--- END SUMMARY ---

--- CONVERSATION HISTORY ---
{history_text}
--- END HISTORY ---

User's current question: {question}

Provide a clear, data-driven answer:
"""
    response = model.generate_content(prompt)
    return response.text

if uploaded_file and api_key:
    df, data_summary = load_and_summarize_data(uploaded_file)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        st.metric("Average Weekly Sales", f"${df['Weekly_Sales'].mean().round(2):,}")
    with col3:
        st.metric("Stores", f"{df['Store'].nunique():,}")

    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "Role": "Assistant",
            "Content": (
                "Hello! I have analysed the Dataset."
                f"It contains **{len(df):,} records** across "
                f"**{df['Store'].nunique()} stores**. "
                "Ask me anything — store performance, holiday impact, "
                "economic factors, sales trends, or anything else!"
            )
        })
    for msg in st.session_state.messages:
        with st.chat_message(msg["Role"]): st.markdown(msg["Content"])
    if prompt := st.chat_input("Ask a question about the Walmart Data..."):
        st.session_state.messages.append({"Role": "User", "Content": prompt})
        with st.chat_message("User"): st.markdown(prompt)
        with st.chat_message("Assistant"):
            with st.spinner("Analyzing Data...."):
                response = get_gemini_response(prompt, data_summary, api_key, st.session_state.messages)
            st.markdown(response)

        st.session_state.messages.append({"Role": "Assistant", "Content": response})

elif not api_key and not uploaded_file:
    st.info("Enter your Gemini Key and Upload the Walmart CSV in the sidebar to get started.")
elif not api_key:
    st.info("Enter your Gemini API Key in the sidebar to get started.")
elif not uploaded_file:
    st.info("Upload the Walmart CSV in the sidebar to get started.")
