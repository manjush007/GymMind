import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
  timeout: 10000,
  headers: { "Content-Type": "application/json" },
});

// Response interceptor for error handling
API.interceptors.response.use(
  (res) => res,
  (err) => {
    console.warn("API error:", err?.message || "Network error");
    return Promise.reject(err);
  }
);

export const chatCore = {
  ask: (message) => API.post("/chat/ask", { message }),
};

export default API;