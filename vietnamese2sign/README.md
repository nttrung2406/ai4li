# Vietnamese to Sign Language Translator

## 🎯 Project Overview

This project implements a Vietnamese to Pakistan Sign Language (PSL) translation system using a web-based interface built with Streamlit. The application bridges the communication gap between Vietnamese speakers and the deaf community by converting Vietnamese text into Pakistan Sign Language video representations.

## 💡 The Idea

The core concept addresses a critical accessibility challenge: **converting Vietnamese text to sign language structure**. This project specifically focuses on:

- **Grammatical Structure Analysis**: Understanding the differences between Vietnamese grammar and sign language structure
- **Cross-Language Translation**: Building a pipeline that converts Vietnamese sentences to sign language through an intermediate language (Urdu)
- **Visual Communication**: Generating actual sign language videos that can be used for communication with the deaf community

This work is particularly valuable for improving accessibility and communication between Vietnamese speakers and sign language users.

### Grammatical Structure Comparison

Understanding the fundamental differences between spoken Vietnamese and Vietnamese Sign Language is crucial for effective translation. The table below illustrates key grammatical contrasts:

| Grammatical Feature | Spoken Vietnamese | Vietnamese Sign Language(s) (General) |
|---------------------|-------------------|----------------------------------------|
| **Primary Word Order** | S-V-O (Subject-Verb-Object)<br>Example: *Tôi đọc sách.* (I read book.) | Topic-Comment (often OSV or Time-OSV)<br>Example: *SÁCH, TÔI ĐỌC.* (BOOK, I READ.) The topic (the book) is established first, then a comment is made about it. |
| **Verbs** | No conjugation. Tense/aspect is marked by helper words.<br>Example: *đã* (past), *đang* (present progressive), *sẽ* (future). | No conjugation. Verbs can be modified for aspect (e.g., repetitive action by repeating the sign). Some verbs are directional—the movement of the sign indicates the subject and object (e.g., the sign for GIVE moves from me to you). |
| **Adjectives/Modifiers** | Follow the noun.<br>Example: *Ngôi nhà màu đỏ.* (House color red.) | Often follow the noun. However, the adjective can be emphasized through facial expression and sign intensity.<br>Example: *NHÀ, ĐỎ.* (HOUSE, RED.) |
| **Questions** | Question words (*ai, gì, ở đâu*) or ending particles (*không, à*).<br>Example: *Bạn ăn cơm chưa?* (You eat rice yet?) | Non-Manual Markers (NMMs). Wh-questions (who, what, where) are accompanied by furrowed eyebrows. Yes/No questions are marked by raised eyebrows and a forward head tilt. |
| **Negation** | Negative word *không* placed before the verb.<br>Example: *Tôi không đọc sách.* (I not read book.) | Negative sign (like KHÔNG or SAI) and/or a negative headshake performed simultaneously with the verb sign. The headshake is a grammatical component. |
| **Classifiers** | Yes, uses classifiers for counting.<br>Example: *một **con** mèo* (one cat), *một **cái** bàn* (one table). | Yes, uses classifiers extensively. But they are handshapes that represent the size, shape, or category of an object. For example, a "flat hand" classifier might represent a table or a book. |
| **Use of Space** | Linear and one-dimensional. Word order is everything. | Three-dimensional and spatial. Locations in the signing space can be used to represent people, places, or ideas. Pointing to a location refers back to what was established there (spatial grammar). |
| **Facial Expressions** | Adds emotional context, but is not strictly grammatical. | Crucial Grammatical Component (NMMs). Eyebrow position, mouth morphemes, and head tilts change the meaning of a sentence, turning a statement into a question or modifying an adverb (e.g., signing CAR with puffed cheeks can mean "a large car" or "a long drive"). |

**Key Insights from this Comparison:**

- **Spatial vs. Linear**: Sign languages utilize three-dimensional space for grammar, while spoken Vietnamese relies on linear word order
- **Non-Manual Markers**: Facial expressions and body language are grammatically essential in sign language, not just emotional additions
- **Topic-Comment Structure**: Sign languages often establish the topic first, then provide commentary, differing from Vietnamese S-V-O structure
- **Directional Verbs**: Sign language verbs can encode subject-object relationships through movement direction
- **Visual Classifiers**: Sign language classifiers are visual representations of object properties, unlike Vietnamese word-based classifiers

## 🏗️ Technical Solution

### Architecture Overview

The translation system follows a multi-stage pipeline:

```
Vietnamese Text → English/Urdu Translation → Text Processing → Sign Language Video
```

### Core Components

#### 1. **Translation Layer**
- **Google Translator**: Converts Vietnamese text to Urdu (intermediate language)
- **Language Bridge**: Uses Urdu as the bridge language to PSL since direct Vietnamese-to-PSL translation isn't available

#### 2. **Text Processing**
- **Token Disambiguation**: Replaces ambiguous words with clearer alternatives
- **Text Cleaning**: Removes punctuation and normalizes text format
- **Safe Tokenization**: Ensures compatibility with sign language translation model

#### 3. **Sign Language Generation**
- **Concatenative Synthesis Model**: Generates sign language videos from processed text
- **Pakistan Sign Language (PSL)**: Target sign language for video output
- **Video Format**: Outputs MP4 videos showing sign language gestures

### Key Technologies

- **Streamlit**: Web application framework for user interface
- **Deep Translator**: Google Translate API integration for Vietnamese-to-Urdu translation
- **Sign Language Translator**: Specialized library for text-to-sign-language conversion
- **Concatenative Synthesis**: AI model for generating sign language videos

## 🔧 Implementation Details

### Translation Pipeline

1. **Input Processing**: 
   - User enters Vietnamese text through web interface
   - Text validation and preprocessing

2. **Language Translation**:
   ```python
   translated = GoogleTranslator(source='vi', target='ur').translate(vietnamese_text)
   ```

3. **Text Disambiguation**:
   ```python
   def disambiguate_tokens(text: str) -> str:
       replacements = {"i": "me"}  # Replace ambiguous pronouns
       # Clean and normalize text
   ```

4. **Sign Language Conversion**:
   ```python
   model = slt.models.ConcatenativeSynthesis(
       text_language="urdu",
       sign_language="psl",
       sign_format="vid"
   )
   ```

5. **Video Generation**: Creates MP4 files with sign language demonstrations

### Model Configuration

- **Text Language**: Urdu (bridge language)
- **Sign Language**: Pakistan Sign Language (PSL)
- **Output Format**: Video (.mp4)
- **Synthesis Method**: Concatenative (combining pre-recorded sign segments)

## 🚀 Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Internet connection (for Google Translate API)
- Sufficient storage space for video outputs

### Installation Steps

1. **Navigate to Project Directory**
   ```bash
   cd vietnamese2sign
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python -c "import streamlit, deep_translator, sign_language_translator; print('All dependencies installed successfully!')"
   ```

### Additional Setup

- **Output Directory**: The application automatically creates an `outputs/` folder for video files
- **Network Access**: Ensure internet connectivity for Google Translate functionality

## 🏃‍♂️ Running the Application

### Start the Application

```bash
streamlit run app.py
```

The application will open in your web browser at `http://localhost:8501`.

### Using the Application

1. **Enter Vietnamese Text**:
   - Type or paste Vietnamese text in the text area
   - Example: "Tôi tên là Nam và tôi yêu khoa học."

2. **Generate Sign Language Video**:
   - Click "🎬 Dịch và tạo Video Ngôn ngữ Ký hiệu"
   - Wait for translation and video generation

3. **View Results**:
   - See the Urdu translation
   - Watch the generated PSL sign language video
   - Videos are saved locally in the `outputs/` folder

### Interface Features

- **Vietnamese Input**: Text area with placeholder examples
- **Real-time Processing**: Progress indicators during translation and video generation
- **Bilingual Interface**: Vietnamese labels with English technical terms
- **Video Playback**: Embedded video player for immediate viewing

## 📊 Features and Capabilities

### Translation Features
- **Vietnamese-to-Urdu Translation**: Leverages Google Translate's robust translation capabilities
- **Text Normalization**: Automatic cleaning and preprocessing of input text
- **Token Disambiguation**: Handles ambiguous words that might confuse the sign language model

### Sign Language Features
- **Video Generation**: Creates actual sign language demonstration videos
- **PSL Support**: Specifically targets Pakistan Sign Language
- **Concatenative Synthesis**: Uses AI to combine sign segments into coherent sentences
- **MP4 Output**: Standard video format for easy sharing and playback

### User Experience Features
- **Intuitive Interface**: Clean, accessible web-based design
- **Vietnamese Localization**: Interface text in Vietnamese for native speakers
- **Error Handling**: Comprehensive error messages and user feedback
- **File Management**: Automatic organization of generated videos

## 🎯 Use Cases

### Educational Applications
- **Sign Language Learning**: Visual demonstration of sign language for Vietnamese concepts
- **Cross-Cultural Communication**: Bridge between Vietnamese and deaf communities
- **Language Research**: Study differences between spoken and sign language structures

### Accessibility Applications
- **Communication Aid**: Assist Vietnamese speakers in communicating with deaf individuals
- **Public Services**: Government offices, hospitals, schools serving diverse communities
- **Emergency Communication**: Critical communication in emergency situations

### Technology Applications
- **API Development**: Foundation for larger accessibility applications
- **Mobile Integration**: Potential for mobile app development
- **Educational Tools**: Integration into learning management systems

## ⚠️ Limitations and Considerations

### Technical Limitations
- **Language Bridge**: Uses Urdu as intermediate language, which may affect translation accuracy
- **Sign Language Scope**: Limited to Pakistan Sign Language (PSL)
- **Internet Dependency**: Requires internet connection for Google Translate
- **Processing Time**: Video generation may take several seconds per sentence

### Translation Accuracy
- **Double Translation**: Vietnamese → Urdu → PSL may introduce translation errors
- **Cultural Context**: Some Vietnamese cultural concepts may not translate directly
- **Grammar Differences**: Sign language structure differs significantly from spoken language

## 🔮 Future Enhancements

### Short-term Improvements
1. **Direct Vietnamese-PSL Translation**: Eliminate intermediate language step
2. **Multiple Sign Languages**: Support for ASL, BSL, and other sign languages
3. **Improved Disambiguation**: More sophisticated text processing
4. **Batch Processing**: Handle multiple sentences simultaneously

### Long-term Vision
1. **Vietnamese Sign Language (VSL)**: Support for Vietnam's native sign language
2. **Real-time Translation**: Live translation from speech to sign language
3. **Mobile Application**: Native mobile apps for Android and iOS
4. **AI Training**: Train models specifically on Vietnamese-to-sign-language data

### Integration Possibilities
1. **Video Calling**: Integration with video conferencing platforms
2. **Educational Platforms**: LMS integration for accessibility
3. **Public Service Integration**: Government and healthcare applications
4. **Social Media**: Social platform accessibility features

