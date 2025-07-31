import streamlit as st
import pandas as pd
from process_vietnamese_text import process_vietnamese_text


st.set_page_config(
    page_title="Vietnamese NLP Pipeline",
    page_icon="🇻🇳",
    layout="wide"
)

st.title("🇻🇳 Vietnamese Text Processing Pipeline")
st.markdown("""
This application demonstrates a basic NLP pipeline for Vietnamese text. It includes:
1.  **Tokenization**: Segmenting a sentence into words, handling compound words (e.g., `Hà_Nội`).
2.  **Part-of-Speech (POS) Tagging**: Identifying the grammatical role of each word (Noun, Verb, etc.).
3.  **Tone Mark Removal**: Normalizing text by removing diacritics (dấu).

Enter a sentence in the text box below or choose a sample to see it in action.
""")

sample_sentences = [
    "Đại học Bách khoa Hà Nội là một trong những trường đại học hàng đầu về kỹ thuật ở Việt Nam.",
    "Cộng hòa Xã hội chủ nghĩa Việt Nam.",
    "Tôi đang học xử lý ngôn ngữ tự nhiên tại thành phố Hồ Chí Minh.",
    "Phở bò rất ngon và là một món ăn nổi tiếng của người Việt."
]

st.subheader("Input Text")
selected_sample = st.selectbox("Or choose a sample sentence:", [""] + sample_sentences)
user_input = st.text_area(
    "Enter your Vietnamese text here:", 
    value=selected_sample, 
    height=150,
    placeholder="Nhập văn bản tiếng Việt của bạn ở đây..."
)

if st.button("Process Text", type="primary") and user_input:
    
    with st.spinner("Processing..."):
        pipeline_results = process_vietnamese_text(user_input)

    st.header("Pipeline Results")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Tokenization (Word Segmentation)")
        st.markdown("Text is segmented into tokens. Compound words are joined by underscores.")
        st.info(f"**Tokenized String:** `{pipeline_results['tokenized_string']}`")
        st.write("**Tokens as a list:**")
        st.json(pipeline_results['tokens_list'])

    with col2:
        st.subheader("3. Tone Mark Removal")
        st.markdown("All Vietnamese tone marks (dấu) are removed from the original text.")
        st.success(f"**Text without tones:** {pipeline_results['no_tones_text']}")


    st.subheader("2. Part-of-Speech (POS) Tagging")
    st.markdown("Each token is assigned a Part-of-Speech tag. See the table and key below.")

    pos_df = pd.DataFrame(pipeline_results['pos_tags'], columns=['Word / Token', 'POS Tag'])
    
    table_col, key_col = st.columns([3, 2])
    with table_col:
        st.dataframe(pos_df, use_container_width=True)
    with key_col:
        st.markdown("""
        **Common POS Tag Key:**
        - **N**: Noun (Danh từ)
        - **Np**: Proper Noun (Danh từ riêng)
        - **V**: Verb (Động từ)
        - **A**: Adjective (Tính từ)
        - **P**: Pronoun (Đại từ)
        - **R**: Adverb (Trạng từ / Phó từ)
        - **L**: Determiner (Lượng từ)
        - **M**: Numeral (Số từ)
        - **E**: Preposition (Giới từ)
        - **C**: Subordinating Conjunction (Liên từ phụ thuộc)
        - **CC**: Coordinating Conjunction (Liên từ kết hợp)
        - **CH**: Punctuation (Dấu câu)
        
        *(Based on the pyvi library's tagset)*
        """)

elif not user_input:
    st.warning("Please enter some text or select a sample sentence and click the 'Process Text' button.")