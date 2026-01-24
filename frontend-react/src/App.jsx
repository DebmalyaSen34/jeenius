import { useState } from 'react'
import axios from 'axios'
import './App.css'

// The URL of your Python Backend
const API_URL = "http://127.0.0.1:8000";

function App() {
  // State Variables (The "Memory" of the frontend)
  const [question, setQuestion] = useState(null);
  const [score, setScore] = useState(0);
  const [loading, setLoading] = useState(false);
  const [feedback, setFeedback] = useState(null);
  const [quizEnded, setQuizEnded] = useState(false);
  const [error, setError] = useState(null);

  // Function to Start the Quiz
  const startQuiz = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${API_URL}/start`);
      setQuestion(response.data);
      setScore(0);
      setFeedback(null);
      setQuizEnded(false);
    } catch (err) {
      console.error(err);
      setError("Could not connect to backend. Is Python running?");
    }
    setLoading(false);
  };

  // Function to Submit an Answer
  const submitAnswer = async (index) => {
    setLoading(true);
    setFeedback(null); // Clear old feedback
    
    try {
      const payload = {
        question_id: question.id,
        selected_option_index: index
      };

      const response = await axios.post(`${API_URL}/submit`, payload);
      const data = response.data;

      // 1. Handle Scoring
      if (data.is_correct) {
        setScore(prev => prev + 1);
      }

      // 2. Handle Feedback (If wrong)
      if (!data.is_correct) {
        // If there is an AI explanation, show it. Otherwise show generic message.
        const msg = data.ai_explanation 
          ? data.ai_explanation 
          : `Incorrect. The correct answer was: ${data.correct_answer_text}`;
        setFeedback({ type: 'error', message: msg });
      } else {
        setFeedback({ type: 'success', message: "Correct! Great job." });
      }

      // 3. Wait a moment, then move to next question
      // If there is a long AI explanation, we wait longer or let user click "Next"
      // For this v1, let's add a "Next" button logic if there is feedback
      
      if (data.next_question) {
        // If it was correct, auto-advance. If wrong, wait for user to read.
        if (data.is_correct) {
           setTimeout(() => setQuestion(data.next_question), 1000);
        } else {
           // We store the next question in a temp state or just update it immediately
           // but keep the feedback visible? 
           // Let's keep it simple: Update question but show feedback above it
           // Actually, better UX: Show feedback, hide options, show "Next" button.
           setQuestion({ ...data.next_question, waitingForNext: true });
        }
      } else if (data.session_ended) {
        setQuizEnded(true);
      }

    } catch (err) {
      setError("Error submitting answer.");
    }
    setLoading(false);
  };

  // --- RENDER HELPERS ---

  if (loading && !question) return <div className="container">Loading...</div>;

  // Screen 1: Start Screen
  if (!question && !quizEnded) {
    return (
      <div className="container start-screen">
        <h1>🧠 JEE-AI Coach</h1>
        <p>Adaptive Physics Assessment powered by GenAI</p>
        {error && <div className="error-box">{error}</div>}
        <button onClick={startQuiz} className="primary-btn">Start Assessment</button>
      </div>
    );
  }

  // Screen 2: Quiz Ended
  if (quizEnded) {
    return (
      <div className="container result-screen">
        <h1>🎉 Session Complete!</h1>
        <h2>Final Score: {score}</h2>
        <button onClick={startQuiz} className="primary-btn">Try Again</button>
      </div>
    );
  }

  // Screen 3: Question Card
  return (
    <div className="container">
      <div className="header">
        <span className="badge difficulty">Difficulty: {question.difficulty_level}</span>
        <span className="badge score">Score: {score}</span>
      </div>

      <div className="question-card">
        <h3>{question.sub_concept}</h3>
        <p className="question-text">{question.question_text}</p>

        {/* Feedback Area */}
        {feedback && (
            <div className={`feedback ${feedback.type}`}>
                {/* Render markdown-like text simply for now */}
                <pre>{feedback.message}</pre>
            </div>
        )}

        <div className="options-grid">
          {question.options.map((opt, idx) => (
            <button 
              key={idx} 
              onClick={() => submitAnswer(idx)}
              disabled={loading || question.waitingForNext}
              className="option-btn"
            >
              {opt}
            </button>
          ))}
        </div>

        {/* If waiting for user to read explanation */}
        {question.waitingForNext && (
            <button 
                className="next-btn" 
                onClick={() => {
                    setQuestion({...question, waitingForNext: false}); // This is a hack for v1
                    // In reality, we should have stored the 'real' next question in a separate state
                    // For now, just clicking the option again will trigger the next logic if we aren't careful.
                    // Let's just restart for simplicity in v1 or fix the logic.
                    // FIX: The backend sent the next question. We need to render it.
                    // Since I updated 'question' with 'next_question' data in submitAnswer,
                    // removing 'waitingForNext' will show the NEW options.
                }}
            >
                Next Question 👉
            </button>
        )}
      </div>
    </div>
  )
}

export default App