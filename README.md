# 🤖 Walmart Sales Data Chatbot

### AI-powered conversational analytics using Google Gemini API + Streamlit

---

## 📌 Project Overview

A fully functional AI chatbot that lets users ask natural language 
questions about the Walmart Weekly Sales dataset and receive 
data-grounded answers powered by Google Gemini API.

Built with Streamlit for the UI, Pandas for data processing, and 
Gemini API with role-based prompting for intelligent responses.

---

## 🛠️ Tech Stack
- **Python** — core language
- **Streamlit** — web app UI with chat interface
- **Google Gemini API** — LLM for natural language responses
- **Pandas** — data loading and statistical summarisation
- **Ngrok** — public URL tunneling for live deployment

---

## ✨ Features
- Upload any CSV dataset and start chatting instantly
- AI responds with exact figures from the dataset
- Maintains conversation history across questions
- 3 live metric cards (total records, avg sales, store count)
- Role-based prompting — Gemini acts as Senior Data Analyst
- Sidebar with API key input and author info
- Fully deployable with a shareable public URL

---

## 💬 Sample Questions
```
Which store has the highest average weekly sales?
How did holiday weeks impact sales vs non-holiday weeks?
What is the effect of unemployment on weekly sales?
Give me 3 actionable recommendations for Walmart management.
Which stores are underperforming and what might be causing it?
```

---

## 📊 Sample Output

![Chatbot Overview](screenshots/chatbot_overview.png)
![Holiday Impact Query](screenshots/holiday_impact_query.png)
![Recommendations Query](screenshots/recommendations_query.png)

---

## 🚀 How to Run

### Step 1 — Clone the repo
```bash
git clone https://github.com/mohitramtekkar5-oss/Walmart-Data-Chatbot
cd Walmart-Data-Chatbot
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Get a free Gemini API key
Visit [aistudio.google.com](https://aistudio.google.com)

### Step 4 — Run the app
```bash
streamlit run app.py
```

### Step 5 — Open in browser
```
http://localhost:8501
```

---

## 💡 Key Learnings
- Streamlit makes it possible to build production-grade 
  data apps in under 100 lines of Python
- Role-based prompting ensures consistent, professional 
  tone across all AI responses
- Caching data summaries with `@st.cache_data` prevents 
  redundant API calls and improves performance
- Conversation history passed to Gemini enables 
  contextually aware multi-turn responses

---

## 🔗 Related Projects
- [AI-Powered Data Insights](https://github.com/mohitramtekkar5-oss/AI-Powered-Data-Insights)
- [Prompt Engineering Experiments](https://github.com/mohitramtekkar5-oss/Prompt-Engineering-Experiments)
- [Walmart Sales Prediction ML](https://github.com/mohitramtekkar5-oss/Walmart-Sales-Prediction-ML)

---

## 👤 Author
**Mohit Priya Ramtekkar**  
Data Analyst | ML & Generative AI Enthusiast  
[LinkedIn](https://linkedin.com/in/mohit-priya-ramtekkar) •
[GitHub](https://github.com/mohitramtekkar5-oss)

---
*Built as part of a hands-on Generative AI learning journey 
following the Generative AI for Everyone course by 
DeepLearning.AI on Coursera.*
