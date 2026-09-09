import { useState } from "react";
import DietPlan from "../components/DietPlan";
import { Reveal } from "../utils/useScrollReveal";
import { getDietPlan } from "../services/dietService";

const GOALS = [
  { key: "muscle_gain", label: "Muscle Gain", icon: "💪", color: "#ff5722" },
  { key: "fat_loss", label: "Fat Loss", icon: "🔥", color: "#f44336" },
  { key: "maintenance", label: "Maintenance", icon: "⚖️", color: "#2979ff" },
  { key: "endurance", label: "Endurance / Cardio", icon: "🏃", color: "#ffc107" },
];

function DietPage() {
  const [selectedGoal, setSelectedGoal] = useState(null);
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");

  const canGenerate = weight && height && selectedGoal;

  const generatePlan = async () => {
    if (!canGenerate) return;
    setLoading(true);
    setError(null);
    setPlan(null);
    try {
      const data = await getDietPlan({ weight: Number(weight), height: Number(height), goal: selectedGoal });
      setPlan(data);
    } catch (err) {
      setError("Could not reach the AI server. Please ensure your backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">

      <Reveal direction="up">
        <div className="accent-line" />
        <h1 className="hero-title">AI Diet Plan 🥗</h1>
        <div className="page-subtitle">Get a personalised meal plan powered by AI</div>
      </Reveal>

      <div className="grid-2">

        {/* Input Panel */}
        <Reveal direction="right" delay={80}>
          <div className="card corner-mark">
            <div className="bracket-title">Your Profile</div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px", marginBottom: "24px" }}>
              <div className="form-group">
                <label className="form-label">Weight (kg)</label>
                <input
                  className="form-input" type="number" placeholder="e.g. 72"
                  value={weight} onChange={(e) => setWeight(e.target.value)}
                  min={30} max={200}
                />
              </div>
              <div className="form-group">
                <label className="form-label">Height (cm)</label>
                <input
                  className="form-input" type="number" placeholder="e.g. 178"
                  value={height} onChange={(e) => setHeight(e.target.value)}
                  min={100} max={250}
                />
              </div>
            </div>

            <div className="form-group">
              <label className="form-label">Fitness Goal</label>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
                {GOALS.map((g) => (
                  <button
                    key={g.key}
                    onClick={() => setSelectedGoal(g.key)}
                    style={{
                      padding: "14px",
                      borderRadius: "var(--radius-sm)",
                      border: `1px solid ${selectedGoal === g.key ? g.color : "var(--border)"}`,
                      background: selectedGoal === g.key ? `${g.color}14` : "var(--bg-primary)",
                      color: selectedGoal === g.key ? g.color : "var(--text-secondary)",
                      cursor: "pointer",
                      fontFamily: "var(--font-display)",
                      fontWeight: 700,
                      fontSize: "0.88rem",
                      letterSpacing: "0.4px",
                      textTransform: "uppercase",
                      display: "flex", alignItems: "center", gap: "8px",
                      transition: "all 0.2s ease",
                      boxShadow: selectedGoal === g.key ? `0 0 12px ${g.color}30` : "none",
                    }}
                  >
                    <span>{g.icon}</span>{g.label}
                  </button>
                ))}
              </div>
            </div>

            <button
              className="btn btn-success"
              style={{ width: "100%", justifyContent: "center", marginTop: "8px" }}
              onClick={generatePlan}
              disabled={loading || !canGenerate}
            >
              {loading ? "⏳ Generating..." : "🥗 Generate Diet Plan"}
            </button>

            {!canGenerate && !loading && (
              <p style={{ fontSize: "0.78rem", color: "var(--text-muted)", textAlign: "center", marginTop: "10px" }}>
                Fill in weight, height, and select a goal to continue.
              </p>
            )}

            {error && <div className="alert alert-error" style={{ marginTop: "16px" }}>⚠️ {error}</div>}
          </div>
        </Reveal>

        {/* Plan Output */}
        <Reveal direction="left" delay={80}>
          <div className="card corner-mark">
            <div className="bracket-title">Your Meal Plan</div>
            {loading ? (
              <div style={{ padding: "48px 0", textAlign: "center", color: "var(--text-muted)" }}>
                <div style={{ fontSize: "2rem", marginBottom: "14px" }}>⏳</div>
                <div style={{ fontFamily: "var(--font-display)", fontWeight: 700, textTransform: "uppercase", color: "var(--text-secondary)" }}>
                  Generating Plan...
                </div>
              </div>
            ) : plan ? (
              <DietPlan {...plan} />
            ) : (
              <div style={{ padding: "48px 0", textAlign: "center", color: "var(--text-muted)" }}>
                <div style={{ fontSize: "2.5rem", marginBottom: "14px" }}>🥗</div>
                <div style={{ fontFamily: "var(--font-display)", fontWeight: 700, textTransform: "uppercase", color: "var(--text-secondary)", marginBottom: "8px" }}>
                  No Plan Yet
                </div>
                <div style={{ fontSize: "0.83rem" }}>Fill in your profile and tap Generate.</div>
              </div>
            )}
          </div>
        </Reveal>
      </div>

      {/* Nutrition Tips */}
      <Reveal direction="up" delay={100}>
        <div className="card corner-mark" style={{ marginTop: "28px" }}>
          <div className="bracket-title">Nutrition Tips</div>
          <div className="grid-3">
            {[
              { icon: "💧", title: "Stay Hydrated", tip: "Drink 8–10 glasses of water daily. Dehydration reduces performance by up to 20%." },
              { icon: "⏰", title: "Meal Timing", tip: "Eat 30–60 min before a workout. Consume protein within 30 min post-session for recovery." },
              { icon: "🌿", title: "Whole Foods First", tip: "Prioritize whole, unprocessed foods — more nutrients, more fibre, better energy levels." },
            ].map((t) => (
              <div key={t.title} style={{
                background: "var(--bg-primary)", borderRadius: "var(--radius-sm)", padding: "20px",
                border: "1px solid var(--border)",
              }}>
                <div style={{ fontSize: "1.8rem", marginBottom: "10px" }}>{t.icon}</div>
                <div style={{ fontFamily: "var(--font-display)", fontWeight: 800, marginBottom: "6px", color: "var(--orange)", textTransform: "uppercase", fontSize: "0.95rem" }}>{t.title}</div>
                <div style={{ fontSize: "0.83rem", color: "var(--text-secondary)", lineHeight: 1.6 }}>{t.tip}</div>
              </div>
            ))}
          </div>
        </div>
      </Reveal>
    </div>
  );
}

export default DietPage;