import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("Welcome! Describe the role you're hiring for.");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const res = await axios.post(
        "https://shl-ai-agent-5v1s.onrender.com/chat",
        {
          messages: [
            {
              role: "user",
              content: message,
            },
          ],
        }
      );

      setReply(res.data.reply);
    } catch (err) {
      setReply("Unable to connect to the backend.");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>

      <div
        style={{
          width: "250px",
          background: "#111827",
          color: "white",
          padding: "20px",
        }}
      >
        <h2>SHL AI</h2>

        <button
          style={{
            width: "100%",
            marginTop: "25px",
            padding: "12px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
          }}
        >
          New Chat
        </button>
      </div>

      <div
        style={{
          flex: 1,
          background: "#0F172A",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <div
          style={{
            color: "white",
            padding: "20px",
            borderBottom: "1px solid #1e293b",
            fontWeight: "bold",
            fontSize: "22px",
          }}
        >
          SHL AI Assessment Recommender
        </div>

        <div
          style={{
            flex: 1,
            padding: "30px",
            color: "white",
          }}
        >
          <div
            style={{
              background: "#1E293B",
              padding: "20px",
              borderRadius: "12px",
            }}
          >
            {loading ? "Thinking..." : reply}
          </div>
        </div>

        <div
          style={{
            display: "flex",
            padding: "20px",
            gap: "10px",
          }}
        >
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your hiring requirement..."
            style={{
              flex: 1,
              padding: "15px",
              borderRadius: "10px",
              border: "none",
            }}
          />

          <button
            onClick={sendMessage}
            style={{
              background: "#2563eb",
              color: "white",
              border: "none",
              padding: "15px 25px",
              borderRadius: "10px",
            }}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;