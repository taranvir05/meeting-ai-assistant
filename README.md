# 🎬 AI Video & Meeting Assistant

An AI-powered meeting assistant that converts **YouTube videos or local audio/video files into structured meeting insights** and allows users to ask questions about the transcript using **Retrieval-Augmented Generation (RAG)**.

The application runs speech-to-text and LLM inference locally, using **OpenAI Whisper** for transcription and **Llama 3.2 3B through Ollama** for analysis and question answering.

## ✨ Features

* 🎥 Process YouTube videos or local audio/video files
* 🎙️ Convert speech into text using Whisper
* 📝 Generate an automatic meeting title
* 📋 Generate a concise meeting summary
* ✅ Extract explicitly mentioned action items
* 🔑 Extract key decisions
* ❓ Identify open questions and follow-up topics
* 💬 Chat with the meeting transcript
* 🔎 Use RAG to retrieve relevant transcript sections before answering questions
* 🧠 Generate embeddings using `all-MiniLM-L6-v2`
* 🗄️ Store and search transcript embeddings using ChromaDB
* 🖥️ Interactive Streamlit interface
* 🔒 Local LLM inference through Ollama

---

## 🏗️ How It Works

```text
YouTube URL / Local File
          ↓
     Audio Processing
          ↓
     Whisper (STT)
          ↓
      Transcript
          │
          ├───────────────┐
          ↓               ↓
   Llama 3.2 3B      MiniLM Embeddings
   via Ollama              ↓
          │           ChromaDB
          │               ↓
          │          Retriever
          │               ↓
          └────────→ Llama 3.2 3B
                         ↓
                    RAG Answer
```

### Processing Pipeline

1. **Input**

   * A YouTube URL or local audio/video file is provided.

2. **Audio Processing**

   * The input is downloaded/processed and divided into manageable audio chunks.

3. **Speech-to-Text**

   * Whisper transcribes the audio locally.

4. **Meeting Analysis**

   * Llama 3.2 3B analyzes the transcript to generate:

     * Meeting title
     * Summary
     * Action items
     * Key decisions
     * Open questions

5. **Vector Database**

   * The transcript is split into smaller chunks.
   * `all-MiniLM-L6-v2` converts these chunks into numerical embeddings.
   * ChromaDB stores the embeddings.

6. **RAG Question Answering**

   * When the user asks a question, the system retrieves the most relevant transcript chunks.
   * These chunks are provided as context to Llama 3.2 3B.
   * The model generates an answer based on the retrieved transcript context.

---

## 🧠 Why RAG?

Instead of sending the entire transcript to the LLM every time a question is asked, the application:

```text
User Question
      ↓
Find relevant transcript chunks
      ↓
Provide those chunks to the LLM
      ↓
Generate answer
```

This helps the assistant focus on the most relevant parts of the meeting and makes the question-answering process more practical for longer transcripts.

---

## 🛠️ Tech Stack

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| Python                | Core application logic               |
| Streamlit             | Web interface                        |
| OpenAI Whisper        | Speech-to-text                       |
| Ollama                | Local LLM runtime                    |
| Llama 3.2 3B          | Summarization and question answering |
| LangChain             | LLM and RAG orchestration            |
| Sentence Transformers | Text embeddings                      |
| all-MiniLM-L6-v2      | Embedding model                      |
| ChromaDB              | Vector database                      |
| yt-dlp                | YouTube media processing             |
| PyDub                 | Audio processing                     |

---

## 📁 Project Structure

```text
meeting-ai-assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── rag_engine.py
│   └── vector_store.py
│
├── utils/
│   └── audio_processor.py
│
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/taranvir05/meeting-ai-assistant.git
cd meeting-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama on your system and download the required model:

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running before starting the application.

### 5. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 💻 Hardware Note

The application performs Whisper transcription and LLM inference locally.

Therefore, processing speed depends on the available hardware. On CPU-based systems, longer videos may take several minutes to process.

The local approach provides the advantage of running the main AI processing without requiring a paid LLM API.

---

## 🔐 Privacy

The project is designed around local AI inference:

* Whisper runs locally.
* Llama 3.2 runs locally through Ollama.
* Transcript embeddings are stored locally using ChromaDB.

No Mistral API key or cloud LLM API is required for the current implementation.

---

## 📸 Screenshots

Add screenshots of the Streamlit application here.

```text
screenshots/
├── dashboard.png
├── meeting-summary.png
└── meeting-chat.png
```

Example:

![Application Dashboard](screenshots/dashboard.png)

---

## 🚀 Future Improvements

* Support larger and faster local LLMs
* Improve processing speed through GPU acceleration
* Add speaker identification
* Add timestamp-based transcript navigation
* Export meeting reports as PDF
* Improve multilingual transcription
* Add persistent storage for multiple meetings
* Deploy the application with a dedicated backend for local/cloud LLM inference

---

## 📌 Project Highlights

This project demonstrates practical implementation of:

* Speech-to-text processing
* Local LLM inference
* Prompt engineering
* LangChain LCEL
* Embeddings
* Vector databases
* Retrieval-Augmented Generation (RAG)
* Streamlit application development
* End-to-end AI application development

---

## 👩‍💻 Author

**Taranvir Kaur**

B.Tech Computer Science Engineering

Interested in **AI/ML, Generative AI, and software development**.
