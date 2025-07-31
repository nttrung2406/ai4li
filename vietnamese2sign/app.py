import streamlit as st
from deep_translator import GoogleTranslator
import sign_language_translator as slt
import os
import re

model = slt.models.ConcatenativeSynthesis(
    text_language="urdu",
    sign_language="psl",        
    sign_format="vid"           # "vid" = return video output
)


def disambiguate_tokens(text: str) -> str:
    """Replace ambiguous tokens with safe alternatives"""
    replacements = {
        "i": "me",  
    }
    # Remove punctuation, lowercase, and replace tokens
    text = re.sub(r"[.,!?]", "", text.lower().strip())
    tokens = text.split()
    tokens = [replacements.get(token, token) for token in tokens]
    return " ".join(tokens)


st.set_page_config(page_title="VN → Sign Language", layout="centered")
st.title("🧏‍♀️ Dịch Văn Bản Tiếng Việt Sang Ngôn Ngữ Ký Hiệu (PSL)")

vietnamese_text = st.text_area("✍️ Nhập văn bản tiếng Việt:", height=150, placeholder="Ví dụ: Tôi tên là Nam và tôi yêu khoa học.")

if st.button("🎬 Dịch và tạo Video Ngôn ngữ Ký hiệu"):
    if not vietnamese_text.strip():
        st.warning("Vui lòng nhập văn bản.")
    else:
        try:
            with st.spinner("🔁 Đang dịch"):
                translated = GoogleTranslator(source='vi', target='ur').translate(vietnamese_text)

            cleaned = disambiguate_tokens(translated)
            st.success(f"Bản dịch `{cleaned}`")

            with st.spinner("Đang chuyển sang Ngôn ngữ Ký hiệu..."):
                sentence = model.translate(cleaned)

                os.makedirs("outputs", exist_ok=True)
                safe_filename = cleaned.replace(" ", "_").lower()
                video_path = f"outputs/{safe_filename}.mp4"
                sentence.save(video_path)

            st.markdown("### Video Ngôn ngữ Ký hiệu (PSL):")
            st.video(video_path)

        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {str(e)}")

