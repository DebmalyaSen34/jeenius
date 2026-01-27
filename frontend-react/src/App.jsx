import { useState } from 'react'
import axios from 'axios'
import './App.css'
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';

// The URL of your Python Backend
const API_URL = "http://127.0.0.1:8000";

function App() {
  // State Variables
  const [token, setToken] = useState(null);
  const [username, setUsername] = useState(null);
  const [authView, setAuthView] = useState('login'); 

  const [question, setQuestion] = useState(null);
  // Holds the next question in memory while user reads explanation for a wrong answer
  const [pendingNextQuestion, setPendingNextQuestion] = useState(null);
  
  const [score, setScore] = useState(0);
  const [loading, setLoading] = useState(false); // General loading (login, start)
  const [submitting, setSubmitting] = useState(false); // Specific answer submission loading
  
  const [feedback, setFeedback] = useState(null);
  const [quizEnded, setQuizEnded] = useState(false);
  const [error, setError] = useState(null);

  const handleAuth = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const formData = new FormData(e.target);
    const user = Object.fromEntries(formData);

    try{
      if (authView === 'signup'){
        await axios.post(`${API_URL}/signup`, user);
        setAuthView('login');
        setError("Registration successful! Please log in.");
      }else{
        const response = await axios.post(`${API_URL}/login`, user);
        const {access_token} = response.data;
        setToken(access_token);
        setUsername(user.username);
      }
    }catch(err){
      console.error(err);
      setError("Authentication failed. Please check your credentials.");
    }
    setLoading(false);
  };

  const logout = () => {
    setToken(null);
    setUsername(null);
    setQuestion(null);
    setScore(0);
    setQuizEnded(false);
  };

  const startQuiz = async () => {
    setLoading(true);
    setError(null);
    try {
      const config = { headers: { Authorization: `Bearer ${token}`}};
      const response = await axios.post(`${API_URL}/tutor/start`, {thread_id: "1"}, config);
      setQuestion(response.data.question);
      setScore(0);
      setFeedback(null);
      setQuizEnded(false);
      setPendingNextQuestion(null);
    } catch (err) {
      console.error(err);
      setError("Could not connect to backend. Is Python running?");
    }
    setLoading(false);
  };

  const submitAnswer = async (index) => {
    setSubmitting(true);
    setFeedback(null); 
    
    try {
      const payload = {
        thread_id: "1",
        selected_option_index: index
      };

      const config = { headers: { Authorization: `Bearer ${token}`}};
      const response = await axios.post(`${API_URL}/tutor/answer`, payload, config);
      
      const { feedback: resultFeedback, next_question } = response.data;

      if (resultFeedback.is_correct) {
        setScore(prev => prev + 1);
        if (next_question) {
            setQuestion(next_question);
            setFeedback(null);
            setPendingNextQuestion(null);
            window.scrollTo(0, 0);
        } else {
            setQuizEnded(true);
        }
      } else {
        setFeedback({
            type: 'incorrect',
            message: resultFeedback.explanation || "That didn't seem right."
        });
        
        if (next_question) {
            setPendingNextQuestion(next_question);
        } else {
            setPendingNextQuestion('END'); 
        }
      }

    } catch(err) {
      console.error(err);
      setError("Error submitting answer. Please try again.");
    }
    setSubmitting(false);
  };

  const loadNextQuestion = () => {
      if (pendingNextQuestion === 'END') {
          setQuizEnded(true);
      } else if (pendingNextQuestion) {
          setQuestion(pendingNextQuestion);
          setPendingNextQuestion(null);
          setFeedback(null);
          window.scrollTo(0, 0);
      }
  };

  // --- Helper to Parse Sections ---
  const renderFeedbackContent = (message) => {
    // Attempt to split by approximate headers provided by LLM
    const cleanText = message.replace(/\r\n/g, '\n');
    
    // Regex logic to find section headers like ## Diagnosis, **Diagnosis**, Diagnosis:
    const diagMatch = cleanText.match(/(?:^|\n)(?:#{1,3}|\*{2})?\s*Diagnosis(?:\*{2}|:)?/i);
    const microMatch = cleanText.match(/(?:^|\n)(?:#{1,3}|\*{2})?\s*Micro-Lesson(?:\*{2}|:)?/i);
    const bridgeMatch = cleanText.match(/(?:^|\n)(?:#{1,3}|\*{2})?\s*Bridge\s*Question(?:\*{2}|:)?/i);

    // Common props for markdown rendering
    const markdownProps = {
        remarkPlugins: [remarkMath],
        rehypePlugins: [rehypeKatex]
    };

    // If structure isn't as expected, fallback to simple markdown
    if (!diagMatch || !microMatch) {
         return (
            <div style={{ textAlign: 'left', background: '#1e1e1e', padding: '15px', borderRadius: '8px', color: '#e0e0e0' }}>
                <ReactMarkdown {...markdownProps}>{message}</ReactMarkdown>
            </div>
         );
    }

    const diagStart = diagMatch.index + diagMatch[0].length;
    const microStart = microMatch.index;
    const microContentStart = microMatch.index + microMatch[0].length;
    
    const diagnosis = cleanText.substring(diagStart, microStart).trim();
    let microLesson = "";
    let bridgeQuestion = "";

    if (bridgeMatch) {
        const bridgeStart = bridgeMatch.index;
        const bridgeContentStart = bridgeMatch.index + bridgeMatch[0].length;
        microLesson = cleanText.substring(microContentStart, bridgeStart).trim();
        bridgeQuestion = cleanText.substring(bridgeContentStart).trim();
    } else {
        microLesson = cleanText.substring(microContentStart).trim();
    }

    const containerStyle = {
        display: 'flex',
        flexDirection: 'row',
        gap: '15px',
        marginTop: '15px',
        flexWrap: 'wrap',
        alignItems: 'stretch'
    };

    const cardStyle = {
        background: '#1e1e1e', // Dark background for cards
        color: '#e0e0e0',       // Light text for high contrast
        borderRadius: '8px',
        padding: '15px',
        flex: 1,                // Distribute space equally
        minWidth: '250px',      // Wrap on small screens
        boxShadow: '0 4px 6px rgba(0,0,0,0.3)', // Slightly stronger shadow for dark mode
        textAlign: 'left',
        borderTop: '4px solid'  // Top border accent
    };

    return (
        <div style={containerStyle}>
            <div style={{ ...cardStyle, borderTopColor: '#e74c3c' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#ff6b6b' }}>🩺 Diagnosis</h4>
                <div style={{ fontSize: '0.95rem', lineHeight: '1.5' }}>
                    <ReactMarkdown {...markdownProps}>{diagnosis}</ReactMarkdown>
                </div>
            </div>
            
            <div style={{ ...cardStyle, borderTopColor: '#3498db' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#5dade2' }}>📚 Micro-Lesson</h4>
                <div style={{ fontSize: '0.95rem', lineHeight: '1.5' }}>
                    <ReactMarkdown {...markdownProps}>{microLesson}</ReactMarkdown>
                </div>
            </div>

            {bridgeQuestion && (
                <div style={{ ...cardStyle, borderTopColor: '#9b59b6' }}>
                    <h4 style={{ margin: '0 0 10px 0', color: '#af7ac5' }}>🌉 Bridge Question</h4>
                    <div style={{ fontSize: '0.95rem', lineHeight: '1.5' }}>
                        <ReactMarkdown {...markdownProps}>{bridgeQuestion}</ReactMarkdown>
                    </div>
                </div>
            )}
        </div>
    );
  };


  // --- RENDER HELPERS ---

  if (!token) {
    return (
      <div className="container auth-screen">
        <h1>🔐 JEE-AI Coach</h1>
        <div className="card" style={{ maxWidth: '400px', margin: '0 auto', padding: '20px', border: '1px solid #ddd', borderRadius: '8px' }}>
          <h2>{authView === 'login' ? 'Login' : 'Sign Up'}</h2>
          {error && <div className="error-box">{error}</div>}
          
          <form onSubmit={handleAuth} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div style={{ textAlign: 'left' }}>
              <label style={{ display: 'block', marginBottom: '5px' }}>Username</label>
              <input name="username" type="text" required style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }} />
            </div>
            <div style={{ textAlign: 'left' }}>
              <label style={{ display: 'block', marginBottom: '5px' }}>Password</label>
              <input name="password" type="password" required style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }} />
            </div>
            <button type="submit" className="primary-btn" disabled={loading}>
              {loading ? 'Processing...' : (authView === 'login' ? 'Login' : 'Sign Up')}
            </button>
          </form>

          <p style={{ marginTop: '15px' }}>
            {authView === 'login' ? "New here? " : "Already have an account? "}
            <button 
              onClick={() => { setError(null); setAuthView(authView === 'login' ? 'signup' : 'login') }}
              style={{ background: 'none', border: 'none', color: '#007bff', cursor: 'pointer', textDecoration: 'underline' }}
            >
              {authView === 'login' ? 'Create Account' : 'Login'}
            </button>
          </p>
        </div>
      </div>
    );
  }

  if (loading && !question) return <div className="container">Starting Session...</div>;

  if (!question && !quizEnded) {
    return (
      <div className="container start-screen">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
            <span>Welcome, <strong>{username}</strong></span>
            <button onClick={logout} className="primary-btn" style={{ fontSize: '0.8rem', padding: '5px 10px', backgroundColor: '#666' }}>Logout</button>
        </div>
        <h1>🧠 JEE-AI Coach</h1>
        <p>Adaptive Physics Assessment powered by GenAI</p>
        {error && <div className="error-box">{error}</div>}
        <button onClick={startQuiz} className="primary-btn">Start Assessment</button>
      </div>
    );
  }

  if (quizEnded) {
    return (
      <div className="container result-screen">
        <h1>🎉 Session Complete!</h1>
        <h2>Final Score: {score}</h2>
        <button onClick={startQuiz} className="primary-btn">Try Again</button>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="header">
        <span className="badge difficulty">Difficulty: {question.difficulty_level.toFixed(2)}</span>
        <span className="badge score">Score: {score}</span>
      </div>

      <div className="question-card">
        <h3>{question.sub_concept}</h3>
        <p className="question-text">{question.question_text}</p>

        <div className="options-grid">
          {question.options.map((opt, idx) => (
            <button 
              key={idx} 
              onClick={() => submitAnswer(idx)}
              disabled={submitting || feedback !== null}
              className="option-btn"
            >
              {opt}
            </button>
          ))}
        </div>

        {submitting && (
            <div style={{ marginTop: '20px', color: '#666', fontStyle: 'italic' }}>
                🤔 Analyzing your logic... <br/>
                <small>If this takes a moment, the AI is likely generating a personalized explanation.</small>
            </div>
        )}

        {/* Updated Feedback Section */}
        {feedback && (
            <div className={`feedback-section ${feedback.type}`} style={{marginTop: '20px'}}>
                {renderFeedbackContent(feedback.message)}
                
                <button 
                    className="next-btn primary-btn" 
                    onClick={loadNextQuestion}
                    style={{ marginTop: '15px', width: '100%' }}
                >
                    Got it, Next Question 👉
                </button>
            </div>
        )}
      </div>
    </div>
  )
}

export default App