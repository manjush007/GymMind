import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import WorkoutPage from "./pages/WorkoutPage";
import DietPage from "./pages/DietPage";
import HabitPage from "./pages/HabitPage";
import ChatBot from "./components/ChatBot";

function App() {
  return (
    <Router>
      <div className="page-wrapper">
        <Navbar />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/workout" element={<WorkoutPage />} />
          <Route path="/diet" element={<DietPage />} />
          <Route path="/habit" element={<HabitPage />} />
        </Routes>
        {/* Floating ChatBot available on all pages */}
        <ChatBot />
      </div>
    </Router>
  );
}

export default App;