import { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import { chatCore } from "../services/api";

const SUGGESTIONS = [
  "Plan a workout 🏋️",
  "Generate diet 🥗",
  "Improve habits 📈",
];

function ChatBot() {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { from: "bot", text: "SYSTEM ALL CLEAR. I am your FIT-AI performance coach. What's your target today?" },
  ]);
  const [typing, setTyping] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, typing]);

  const sendMessage = async (text = input) => {
    const trimmed = text.trim();
    if (!trimmed) return;

    // Add user message to UI immediately
    setMessages((prev) => [...prev, { from: "user", text: trimmed }]);
    setInput("");
    setTyping(true);

    try {
      // Call the FastAPI Gemini endpoint
      const response = await chatCore.ask(trimmed);
      setMessages((prev) => [...prev, { from: "bot", text: response.data.reply }]);
    } catch (error) {
      console.error("Chat API Error:", error);
      setMessages((prev) => [...prev, { from: "bot", text: "Connection error. Please check if the AI module is online and configured." }]);
    } finally {
      setTyping(false);
    }
  };

  const handleKey = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="chatbot-float">
      {open && (
        <div className="chatbot-window sport-angled">
          {/* Header */}
          <div className="chatbot-header">
            <div className="chatbot-avatar">
              <span className="live-pulse"></span>
              AI
            </div>
            <div className="chatbot-header-info">
              <h4>FIT-AI COACH</h4>
              <p className="status-text">ONLINE · READY</p>
            </div>
            <button className="chat-close" onClick={() => setOpen(false)}>×</button>
          </div>

          {/* Messages */}
          <div className="chatbot-messages hide-scrollbar">
            {messages.map((msg, i) => (
              <div key={i} className={`chat-wrapper ${msg.from}`}>
                <div className={`chat-msg ${msg.from}`}>
                  {msg.text}
                </div>
              </div>
            ))}

            {/* Quick Suggestions (only if bot just spoke and few messages) */}
            {!typing && messages.length < 4 && messages[messages.length - 1].from === "bot" && (
              <div className="chat-suggestions">
                {SUGGESTIONS.map((s, i) => (
                  <button key={i} onClick={() => sendMessage(s)} className="suggest-chip">{s}</button>
                ))}
              </div>
            )}

            {typing && (
              <div className="chat-wrapper bot">
                <div className="chat-msg bot typing-indicator">
                  <span></span><span></span><span></span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="chatbot-input-area">
            <input
              type="text"
              placeholder="Ask me anything..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKey}
            />
            <button className="send-btn" onClick={() => sendMessage()}>&#10148;</button>
          </div>
        </div>
      )}

      {/* Floating Toggle */}
      {!open && (
        <button className="chatbot-toggle pulse-ring" onClick={() => setOpen(true)}>
          <span className="icon">💬</span>
        </button>
      )}
    </div>
  );
}

export default ChatBot;