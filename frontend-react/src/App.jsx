import { useState, useEffect } from 'react';
import axios from 'axios';
import { InlineMath, BlockMath } from 'react-katex';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import 'katex/dist/katex.min.css';
import './App.css';

const API_URL = "http://127.0.0.1:8000";

// --- NEW: The "Smart" Renderer ---
// This component understands both Markdown and LaTeX.
function MarkdownRenderer({ text }) {
  if (!text) return null;
  return (
    <ReactMarkdown
      remarkPlugins={[remarkMath]}
      components={{
        // This tells the renderer how to display math
        'p': ({ children }) => <p className="markdown-p">{children}</p>,
        'h3': ({ children }) => <h3 className="markdown-h3">{children}</h3>,
        'ul': ({ children }) => <ul className="markdown-ul">{children}</ul>,
        'li': ({ children }) => <li className="markdown-li">{children}</li>,
        'code': ({node, inline, className, children, ...props}) => {
           const match = /language-(\w+)/.exec(className || '')
           if (!inline && match) {
             // This is for code blocks, not relevant for us but good practice
             return <code className={className} {...props}>{children}</code>
           }
           // This is for inline math ($...$)
           return <InlineMath math={String(children)} />
        }
      }}
    >
      {text}
    </ReactMarkdown>
  );
}

// --- Dynamic Loading Component (Unchanged) ---
function FeedbackLoader({ concept }) {
  const [message, setMessage] = useState("🤖 Analyzing your mistake...");
  useEffect(() => {
    const timer = setTimeout(() => {
      setMessage(`Hmm, looks like a slip-up in "${concept}". Checking the knowledge base...`);
    }, 2500);
    return () => clearTimeout(timer);
  }, [concept]);
  return <div className="loading-text">{message}</div>;
}

function App() {
  const [gameState, setGameState] = useState('start');
  const [question, setQuestion] = useState(null);
  const [score, setScore] = useState(0);
  const [error, setError] = useState(null);
  const [answerResult, setAnswerResult] = useState(null);
  const [nextQuestionData, setNextQuestionData] = useState(null);

  const startQuiz = async () => {
    setGameState('loading');
    setError(null);
    setAnswerResult(null);
    setNextQuestionData(null);
    try {
      const response = await axios.post(`${API_URL}/start`);
      setQuestion(response.data);
      setScore(0);
      setGameState('quiz');
    } catch (err) {
      setError("Could not connect to backend. Is the Python server running?");
      setGameState('start');
    }
  };

  const submitAnswer = async (selectedIndex) => {
    const correctIndex = question.correct_option_index;
    const isCorrect = selectedIndex === correctIndex;

    setAnswerResult({
      isCorrect,
      correctIndex,
      selectedIndex,
      isLoading: !isCorrect,
      aiExplanation: null
    });

    if (isCorrect) {
      setScore(prev => prev + 1);
    }

    try {
      const payload = {
        question_id: question.id,
        selected_option_index: selectedIndex
      };
      const response = await axios.post(`${API_URL}/submit`, payload);
      const data = response.data;

      if (data.next_question) {
        setNextQuestionData(data.next_question);
      } else {
        // No more questions, prepare to end the session
        setNextQuestionData(null); 
      }

      if (!isCorrect) {
        setAnswerResult(prev => ({ ...prev, isLoading: false, aiExplanation: data.ai_explanation }));
      }
    } catch (err) {
      setError("Error getting feedback from AI Coach.");
      if (!isCorrect) {
        setAnswerResult(prev => ({ ...prev, isLoading: false }));
      }
    }
  };

  const handleNext = () => {
    if (nextQuestionData) {
      setQuestion(nextQuestionData);
      setNextQuestionData(null);
      setAnswerResult(null);
    } else {
      // If there's no next question, end the game
      setGameState('ended');
      setAnswerResult(null); // Clear the result for the end screen
    }
  };

  // --- RENDER LOGIC ---

  if (gameState === 'loading') {
    return <div className="container"><h1>Loading Assessment...</h1></div>;
  }

  if (gameState === 'start' || gameState === 'ended') {
    return (
      <div className="container start-screen">
        <h1>{gameState === 'ended' ? '🎉 Session Complete!' : '🧠 JEE-AI Coach'}</h1>
        {gameState === 'ended' && <h2>Final Score: {score}</h2>}
        <p>Adaptive Physics Assessment powered by GenAI</p>
        {error && <div className="error-box">{error}</div>}
        <button onClick={startQuiz} className="primary-btn">
          {gameState === 'ended' ? 'Try Again' : 'Start Assessment'}
        </button>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="header">
        <span className="badge difficulty">Difficulty: {question.difficulty_level}</span>
        <span className="badge score">Score: {score}</span>
      </div>

      <div className="question-card">
        <h3>{question.sub_concept}</h3>
        {/* Use the new MarkdownRenderer for the question text */}
        <div className="question-text">
          <MarkdownRenderer text={question.question_text} />
        </div>

        <div className="options-grid">
          {question.options.map((opt, idx) => {
            let buttonClass = 'option-btn';
            if (answerResult) {
              if (idx === answerResult.correctIndex) buttonClass += ' correct';
              else if (idx === answerResult.selectedIndex) buttonClass += ' incorrect';
            }
            return (
              <button 
                key={idx} 
                onClick={() => submitAnswer(idx)}
                disabled={answerResult}
                className={buttonClass}
              >
                {/* Use the renderer for options too! */}
                <MarkdownRenderer text={opt} />
              </button>
            )
          })}
        </div>

        {answerResult && (
          <div className="feedback-container">
            {answerResult.isLoading ? (
              <FeedbackLoader concept={question.sub_concept} />
            ) : answerResult.aiExplanation ? (
              <MarkdownRenderer text={answerResult.aiExplanation} />
            ) : (
              <p>✅ Correct! Well done.</p>
            )}
          </div>
        )}
        
        {answerResult && !answerResult.isLoading && (
          <button className="next-btn" onClick={handleNext}>
            {nextQuestionData ? 'Next Question 👉' : 'Finish Session'}
          </button>
        )}
      </div>
    </div>
  )
}

export default App;