# JEEnius (JEE-AI) 🎓🚀

**An AI-Powered Personalized Tutor for JEE Preparation**

JEEnius is an intelligent tutoring system designed to help students master complex physics concepts for the Joint Entrance Examination (JEE). Unlike traditional quiz apps, JEEnius uses **Retrieval-Augmented Generation (RAG)** to provide context-aware explanations and **Adaptive Scoring** to distinguish between simple mistakes and deep conceptual gaps.

---

## 🌟 Key Features

*   **🧠 Intelligent RAG Tutor:** Uses **Google Gemini** models to analyze student mistakes and provide explanations grounded in standard textbooks (e.g., NCERT, H.C. Verma). retrieval is powered by a **FAISS** vector database.
*   **🎯 Adaptive Assessment:** Goes beyond binary "Correct/Incorrect" grading. The AI evaluates the *severity* of an error on a 1-5 scale to determine if a student needs a hint, a full explanation, or a remedial lesson.
*   **📚 Automated Content Pipeline:** Converts raw PDF textbooks into structured JSON data (questions, options, logic) using LLMs.
*   **⚡ Modern Stack:** Built with a high-performance **FastAPI** backend and a responsive **React (Vite)** frontend.

---

## 🏗️ Architecture

### High-Level Flow
1.  **Question Delivery:** The system presents a physics problem from the curated Question Bank.
2.  **User Answer:** The student selects an answer.
3.  **Initial Check:** The system verifies correctness against the key.
4.  **AI Analysis (If Wrong):**
    *   **Scoring Agent:** Analyzes the logic of the wrong answer.
    *   **RAG Retrieval:** Fetches relevant theory from the vector database (`faiss_index`).
    *   **Tutor Agent:** Generates a personalized explanation using the retrieved context.
5.  **Feedback:** The frontend displays the specific feedback to the user.

### Tech Stack

**Backend**
*   **Framework:** FastAPI (Python)
*   **AI Orchestration:** LangChain
*   **LLMs:** Google Gemini 1.5/2.5 Flash, Ollama (Local Fallback)
*   **Vector DB:** FAISS (Facebook AI Similarity Search)
*   **Embeddings:** `all-MiniLM-L6-v2` (HuggingFace)
*   **Database:** SQLite (via SQLAlchemy)

**Frontend**
*   **Framework:** React (Vite)
*   **Styling:** CSS Modules / Standard CSS
*   **Math Rendering:** KaTeX (`react-markdown`, `rehype-katex`) for rendering complex physics formulas.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js & npm
*   Google Gemini API Key

### 1. Clone the Repository
```bash
git clone <repository-url>
cd jeenius

2. Backend Setup
Navigate to the backend directory and set up the Python environment.

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


jeenius/
├── backend/
│   ├── app/
│   │   ├── agent/          # AI Agents (Tutor, Scorer, RAG Engine)
│   │   ├── api/            # API Routes (Auth, Tutor, User)
│   │   ├── core/           # Configuration & Security
│   │   ├── db/             # Database Models & Session
│   │   └── main.py         # FastAPI Entrypoint
│   ├── data/               # Raw books & Processed JSONs
│   ├── faiss_index/        # Vector Database Storage
│   └── utils/              # Data Processing Scripts (PDF -> JSON, Build KB)
│
├── frontend-react/
│   ├── src/                # React Source Code
│   ├── package.json        # Frontend Dependencies
│   └── vite.config.js      # Vite Configuration
│
└── log.md                  # Development Log & Roadmap

🔮 Roadmap
v0.1.0 (Current): Basic RAG Pipeline, Terminal Prototype -> Web App Migration.
v0.2.0 (Planned):
Full State Management (Tracking student history).
Smarter Item Response Theory (IRT) for question selection.
Dashboards for progress visualization.
