
# JEE-AI: Adaptive Learning Coach 🧠

**JEE-AI** is an intelligent, SAT-inspired adaptive learning platform designed for Physics (Mechanics). Unlike standard quiz apps, it uses Generative AI to diagnose *why* a student failed and provides targeted, RAG-powered remediation in real-time.

---

## 🌟 Key Features (v1 Prototype)

*   **📄 Automated Content Pipeline:** Extracts structured questions directly from PDF textbooks using Multimodal LLMs.
*   **🤖 RAG-Powered Tutor:** Explains concepts by retrieving verified theory from a vector database (no hallucinations).
*   **⚖️ AI Severity Scoring:** Distinguishes between "silly mistakes" and "conceptual gaps" to decide when to intervene.
*   **🔄 Adaptive Loop:** A terminal-based engine that simulates the student-tutor interaction cycle.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.10+
*   **LLMs:** Google Gemini 1.5 Flash (Data Extraction), Gemini 2.5 Flash (Tutoring & Scoring)
*   **Orchestration:** LangChain
*   **Vector Database:** FAISS (Facebook AI Similarity Search)
*   **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

git clone <your-repo-url>
cd jee-ai
2. Set up Virtual Environment
code
Bash

download

content_copy

expand_less
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
code
Bash

download

content_copy

expand_less
pip install -r requirements.txt
4. Configure API Keys
Create a .env file in the root directory:

code
Bash

download

content_copy

expand_less
touch .env
Add your Google Gemini API key:


GEMINI_API_KEY="your_api_key_here"
🏃‍♂️ How to Run

Step 1: Build the Knowledge Base (One-time setup)
This indexes the physics theory into the vector database.

python build_kb.py

Step 2: Generate Question Bank (Optional)
Note: A pre-processed question_bank.json is included in data/processed/.
To regenerate it from a PDF:


python scripts/book_to_json.py


Step 3: Start the Coach
Run the interactive terminal application:

python main_engine.py



📂 Project Structure

jee-ai/
├── data/
│   ├── processed/       # JSONs and Theory files
│   └── raw/             # PDF Textbooks
├── faiss_index/         # Vector Database (Generated)
├── scripts/             # Data pipeline scripts
│   └── book_to_json.py
├── build_kb.py          # Knowledge Base Indexer
├── genai_tutor.py       # RAG Logic
├── scoring_logic.py     # AI Severity Evaluator
├── main_engine.py       # Main Application Loop
└── requirements.txt



🔮 Future Roadmap

Migrate to FastAPI backend.
Implement Pydantic models for strict data validation.
Add Item Response Theory (IRT) for difficulty adjustment.
Build a React/Next.js Frontend.


### 3. How to Push to GitHub (Safely)

Now, let's push this to GitHub. **Crucial:** We must ensure your `.env` file (with the API key) is NOT uploaded.

1.  **Check `.gitignore`:**
    Make sure you have a file named `.gitignore` in your root folder with at least these lines:
    ```text
    .env
    venv/
    __pycache__/
    faiss_index/
    *.DS_Store
    ```

2.  **Initialize Git:**
    ```bash
    git init
    ```

3.  **Add Files:**
    ```bash
    git add .
    ```

4.  **Commit:**
    ```bash
    git commit -m "v1.0: Functional Terminal Prototype with RAG and AI Scoring"
    ```

5.  **Push:**
    *   Go to GitHub.com and create a new **empty** repository named `jee-ai`.
    *   Copy the commands under "…or push an existing repository from the command line".
    *   Run them in your terminal:
    ```bash
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/jee-ai.git
    git push -u origin main
    ```
