
import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Briefly AI | Text Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f6f8ff 0%, #eef2ff 100%);
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        background: linear-gradient(120deg, #172554, #4338ca);
        padding: 32px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 28px rgba(49, 46, 129, 0.18);
    }

    .hero h1 {
        font-size: 38px;
        margin: 0 0 10px 0;
        color: white;
    }

    .hero p {
        font-size: 16px;
        margin: 0;
        color: #e0e7ff;
    }

    .panel {
        background: white;
        padding: 22px;
        border: 1px solid #e0e7ff;
        border-radius: 18px;
        min-height: 180px;
        box-shadow: 0 4px 18px rgba(30, 41, 59, 0.05);
    }

    .panel h3 {
        color: #312e81;
    }

    .stButton > button {
        background: linear-gradient(90deg, #4338ca, #6366f1);
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 48px;
        font-weight: 600;
        width: 100%;
    }

    .stButton > button:hover {
        color: white;
        border: 1px solid #818cf8;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding-top: 25px;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- MODEL ----------------
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


@st.cache_resource(show_spinner=False)
def load_summarizer():
    return pipeline(
        task="summarization",
        model=MODEL_NAME,
        device=-1
    )


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 📝 Briefly AI")
    st.caption("AI-powered text summarization")

    st.divider()

    summary_style = st.selectbox(
        "Summary length",
        ["Short", "Balanced", "Detailed"],
        index=1
    )

    st.markdown("### How it works")
    st.markdown(
        "1. Enter your text\n"
        "2. Select summary length\n"
        "3. Generate your summary\n"
        "4. Download the result"
    )

    st.divider()
    st.caption("Model: DistilBART CNN/DailyMail")
    st.caption("Powered by Hugging Face Transformers")


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>✨ Briefly AI</h1>
    <p>Turn lengthy text into clear, meaningful summaries.</p>
    <p>Less reading. More understanding.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT ----------------
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("### 📄 Original Text")
    input_text = st.text_area(
        "Paste your article or text below",
        height=300,
        placeholder=(
            "Paste an article, study material, report, "
            "or other English text here..."
        ),
        label_visibility="collapsed"
    )

    word_count = len(input_text.split())
    st.caption(f"Original word count: {word_count:,}")

    generate = st.button(
        "✨ Generate Summary",
        use_container_width=True
    )

with right:
    st.markdown("### 🧠 AI Summary")

    if "summary_result" not in st.session_state:
        st.session_state.summary_result = ""

    if generate:
        if not input_text.strip():
            st.warning("Please enter some text first.")

        elif word_count < 30:
            st.warning(
                "Please enter at least 30 words for a "
                "more useful summary."
            )

        else:
            # DistilBART has a limited input token length.
            # Tokenization truncates very long input.
            length_settings = {
                "Short": (25, 70),
                "Balanced": (45, 120),
                "Detailed": (70, 160)
            }

            min_len, max_len = length_settings[summary_style]

            try:
                with st.spinner(
                    "Loading AI model and generating summary..."
                ):
                    summarizer = load_summarizer()

                    result = summarizer(
                        input_text,
                        max_length=max_len,
                        min_length=min_len,
                        do_sample=False,
                        truncation=True
                    )

                    st.session_state.summary_result = (
                        result[0]["summary_text"]
                    )

            except Exception as error:
                st.error(
                    "Unable to generate the summary. "
                    "Check your internet connection on the "
                    "first run and verify that the required "
                    "libraries are installed."
                )
                st.caption(f"Technical details: {error}")

    summary = st.session_state.summary_result

    if summary:
        st.markdown(
            f'<div class="panel">{summary}</div>',
            unsafe_allow_html=True
        )

        summary_words = len(summary.split())
        reduction = (
            (1 - summary_words / word_count) * 100
            if word_count else 0
        )

        st.markdown("")
        metric1, metric2 = st.columns(2)

        metric1.metric(
            "Summary words",
            f"{summary_words:,}"
        )

        metric2.metric(
            "Text reduction",
            f"{max(0, reduction):.1f}%"
        )

        st.download_button(
            label="⬇️ Download Summary",
            data=summary,
            file_name="briefly_ai_summary.txt",
            mime="text/plain",
            use_container_width=True
        )

    else:
        st.markdown("""
        <div class="panel">
            <h3>💡 Your summary will appear here</h3>
            <p style="color:#64748b">
                Add your text on the left and click
                Generate Summary to see the result.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Briefly AI · Built with Streamlit and Hugging Face Transformers
    <br>AI-generated summaries may omit details. Please verify important information.
</div>
""", unsafe_allow_html=True)
