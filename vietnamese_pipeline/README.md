# Vietnamese NLP Pipeline for Sign Language Processing

## 🎯 Project Overview

This project implements a comprehensive Natural Language Processing (NLP) pipeline specifically designed for Vietnamese text processing, with a focus on supporting sign language conversion. The application provides a web-based interface built with Streamlit that demonstrates core NLP techniques including tokenization, part-of-speech tagging, and tone mark processing.

## 💡 The Idea

The project addresses two main objectives:

1. **Vietnamese Text Processing Pipeline**: Build a robust pipeline for processing Vietnamese text including tokenization, POS tagging, and tone mark handling with sample sentence testing.

2. **Sign Language Processing Foundation**: Analyze grammatical structure differences between Vietnamese and sign language, laying the groundwork for a system that converts Vietnamese sentences to sign language structure.

This work is particularly valuable for the deaf and hard-of-hearing community, as it provides tools for better text processing and potentially facilitates communication through sign language conversion.

## Project Structure

The project is organized into modular components for better maintainability and reusability:

```
NLP_pipeline_for_deaf/
├── app.py                     # Main Streamlit web application
├── process_vietnamese_text.py # Core NLP processing pipeline
├── remove_tones.py           # Vietnamese tone mark removal utility
├── requirements.txt          # Project dependencies
├── issue.txt                # Project objectives and requirements
└── README.md                # This documentation
```

### Module Descriptions

#### `app.py`
- **Purpose**: Main Streamlit web application providing the user interface
- **Features**: 
  - Interactive text input with sample sentences
  - Real-time processing and results display
  - Comprehensive POS tag reference guide
  - Responsive two-column layout for results

#### `process_vietnamese_text.py`
- **Purpose**: Core NLP processing pipeline
- **Features**:
  - Vietnamese text tokenization using PyVi
  - Part-of-speech tagging
  - Integration with tone removal functionality
  - Structured output with detailed results

#### `remove_tones.py`
- **Purpose**: Utility for Vietnamese tone mark removal
- **Features**:
  - Unicode normalization (NFD) for diacritic separation
  - Clean removal of Vietnamese tone marks
  - Useful for text normalization and search optimization

## Technical Solution

### Core Technologies

- **PyVi**: Vietnamese NLP library for tokenization and POS tagging
- **Streamlit**: Web application framework for interactive UI
- **Pandas**: Data manipulation for result display
- **Unicode**: Standard text normalization for tone processing

### Processing Pipeline

1. **Tokenization**: 
   - Segments Vietnamese text into meaningful tokens
   - Handles compound words with underscore joining (e.g., `Hà_Nội`)
   - Uses PyVi's `ViTokenizer` for accurate segmentation

2. **Part-of-Speech Tagging**:
   - Identifies grammatical roles of each word
   - Provides detailed POS tags (Noun, Verb, Adjective, etc.)
   - Uses PyVi's `ViPosTagger` for Vietnamese-specific tagging

3. **Tone Mark Processing**:
   - Removes Vietnamese diacritical marks (dấu)
   - Normalizes text for search and comparison
   - Preserves original text structure

### Output Structure

The pipeline returns a comprehensive dictionary containing:
- `original_text`: Input text unchanged
- `tokenized_string`: Text with properly segmented compound words
- `tokens_list`: Individual tokens as a list
- `pos_tags`: Word-tag pairs for grammatical analysis
- `no_tones_text`: Text with tone marks removed

**Sample output:**

![alt text](result.png)


## Setup and Installation

### Prerequisites

- Python 3.7 or higher
### Installation Steps

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd NLP_pipeline_for_deaf
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```


## 🏃Running the Application

### Start the Streamlit Web Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

### Using the Application

1. **Text Input**: 
   - Enter Vietnamese text in the text area
   - Or select from pre-defined sample sentences

2. **Processing**: 
   - Click the "Process Text" button
   - View real-time processing with spinner indicator

3. **Results**: 
   - Tokenization results with compound word handling
   - Comprehensive POS tagging table with reference guide
   - Tone-removed text for normalization purposes

### Sample Sentences Included

- University and technical education context
- Political and governmental terms
- Natural language processing terminology
- Cultural food references

## Use Cases

### Educational Applications
- Vietnamese language learning and analysis
- Linguistic research on Vietnamese grammar
- NLP technique demonstration and teaching

### Accessibility Applications
- Text preprocessing for sign language conversion
- Communication assistance for deaf community
- Multilingual accessibility tool development

### Technical Applications
- Vietnamese text normalization for search engines
- Content analysis and grammatical structure research
- Foundation for advanced Vietnamese NLP applications

## Features and Capabilities

### Comprehensive Text Analysis
- **Word Segmentation**: Accurate Vietnamese tokenization
- **Grammatical Analysis**: Detailed POS tagging with 12+ tag types
- **Text Normalization**: Tone mark removal for standardization

### User-Friendly Interface
- **Interactive Design**: Clean, responsive Streamlit interface
- **Real-time Processing**: Immediate results with visual feedback
- **Educational Content**: Built-in POS tag reference guide

### Modular Architecture
- **Separation of Concerns**: Each function in dedicated modules
- **Reusability**: Easy integration into other projects
- **Maintainability**: Clear structure for future enhancements

## Future Enhancements

1. **Sign Language Integration**: Complete the Vietnamese-to-sign-language conversion system
2. **Advanced NLP Features**: Named entity recognition, sentiment analysis
3. **Multi-language Support**: Extend to other Southeast Asian languages
4. **API Development**: RESTful API for integration with other applications
5. **Mobile Application**: Native mobile app for accessibility
