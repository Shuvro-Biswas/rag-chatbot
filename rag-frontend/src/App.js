import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setAnswer("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/query", {
        query: query,
      });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("❌ Error fetching response from backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-8 col-md-10">
          <div className="card shadow-lg border-0">
            <div className="card-header bg-primary text-white text-center">
              <h3 className="mb-0"> Multilingual RAG Chatbot</h3>
              <small>Ask questions in English or Bengali</small>
            </div>
            <div className="card-body p-4">
              <form onSubmit={handleSubmit} className="d-flex gap-2">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Type your question..."
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  required
                />
                <button
                  type="submit"
                  className="btn btn-success"
                  disabled={loading}
                >
                  {loading ? "Thinking..." : "Ask"}
                </button>
              </form>

              <div className="mt-4">
                <h5 className="text-muted">Answer:</h5>
                <div className="bg-light p-3 rounded border">
                  {answer ? (
                    <p className="mb-0">{answer}</p>
                  ) : (
                    <p className="text-secondary mb-0">No answer yet.</p>
                  )}
                </div>
              </div>
            </div>
            <div className="card-footer text-muted text-center small">
              © 2025 AI RAG Assistant | Powered by FastAPI + React
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
