# Development Log - JEE-AI

## v0.1.0 - The "Terminal Prototype" (Current Version)
**Date:** January 24, 2026
**Focus:** Core Logic & RAG Pipeline Implementation

### 🚀 Achievements
We have successfully built the "Vertical Slice" of the application. The system runs entirely in the terminal but contains all the intelligent components required for the final product.

### 🛠️ Technical Decisions & Architecture

#### 1. Data Pipeline (`scripts/book_to_json.py`)
*   **Challenge:** We needed to convert raw PDF textbooks into structured JSON data (Questions, Options, Logic).
*   **Solution:** Used **Gemini 1.5 Flash**.
*   **Why:** It is the only stable model with a massive context window (1M+ tokens) capable of ingesting a whole PDF chapter natively. Local models (Gemma/Llama) failed here due to context limits.
*   **Hurdle:** Encountered dependency conflicts between `google-generativeai` and `google-genai`. Solved by forcing a clean reinstall of `google-generativeai` (0.8.6).

#### 2. Knowledge Base (`build_kb.py`)
*   **Challenge:** The AI needs a "textbook" to reference when teaching.
*   **Solution:** Created a **FAISS** vector store using **LangChain**.
*   **Embeddings:** Used `all-MiniLM-L6-v2` (HuggingFace). It runs locally on the Mac, is fast, and free.

#### 3. The RAG Tutor (`genai_tutor.py`)
*   **Challenge:** Generating explanations that are accurate and don't hallucinate physics formulas.
*   **Solution:** Implemented Retrieval-Augmented Generation (RAG).
    1.  **Retrieve:** Search FAISS for the specific physics concept.
    2.  **Augment:** Feed that concept text into the prompt.
    3.  **Generate:** Use **Gemini 2.5 Flash** to act as the tutor.

#### 4. Assessment Intelligence (`scoring_logic.py`)
*   **Challenge:** Binary scoring (Correct/Incorrect) is too simple for adaptive learning.
*   **Solution:** Created an AI evaluator using Gemini 2.5 Flash (Temperature 0.0).
*   **Logic:** It analyzes the student's wrong answer against the correct logic and assigns a **Severity Score (1-5)**.
    *   1-2: Silly mistakes (keep going).
    *   3-5: Conceptual gaps (trigger Tutor).

#### 5. The Main Engine (`main_engine.py`)
*   **Status:** A synchronous Python script that ties all modules together in a `while` loop.
*   **Flow:** Load Questions -> Ask User -> Check Answer -> (If Wrong) AI Score -> (If Severe) RAG Tutor Intervention.

---

### 🔮 Next Steps (Roadmap to v0.2.0)
1.  **State Management:** Move from local variables to a structured `AssessmentState` object.
2.  **Backend API:** Refactor `main_engine.py` into a **FastAPI** application.
3.  **Item Selector:** Implement the logic to pick the *next* question based on difficulty, rather than iterating sequentially.