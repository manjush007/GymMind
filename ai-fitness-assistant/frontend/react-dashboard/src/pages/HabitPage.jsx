import { useState } from "react";
import HabitTracker from "../components/HabitTracker";
import { Reveal } from "../utils/useScrollReveal";
import { getHabitPrediction } from "../services/habitService";

function HabitPage() {
  const [sleep, setSleep] = useState(7);
  const [stress, setStress] = useState(5);
  const [workout, setWorkout] = useState(null);   // null = not answered yet
  const [hydration, setHydration] = useState(6);
  const [consistency, setConsistency] = useState(50);

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const canSubmit = workout !== null;

  const runPrediction = async () => {
    if (!canSubmit) return;
    setLoading(true);
    setError(null);
    setPrediction(null);
    try {
      const data = await getHabitPrediction({
        sleep, stress, workout: workout ? 1 : 0, hydration, consistency,
      });
      setPrediction(data);
    } catch {
      setError("Could not reach the AI server. Make sure your backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const riskColor =
    prediction?.risk === "high" ? "#f44336" :
      prediction?.risk === "medium" ? "#ffc107" :
        prediction?.risk === "low" ? "#ff5722" :
          "var(--text-muted)";

  return (
    <div className="page-container">

      <Reveal direction="up">
        <div className="accent-line" />
        <h1 className="hero-title">Habit Analysis 📊</h1>
        <div className="page-subtitle">Track lifestyle metrics and predict workout adherence</div>
      </Reveal>

      <div className="grid-2">

        {/* Input Panel */}
        <Reveal direction="right" delay={80}>
          <div className="card corner-mark">
            <div className="bracket-title">Today's Input</div>

            {[
              { label: `Sleep: ${sleep} hrs`, val: sleep, set: setSleep, min: 3, max: 12, step: 0.5 },
              { label: `Stress Level: ${stress}/10`, val: stress, set: setStress, min: 1, max: 10, step: 1 },
              { label: `Hydration: ${hydration} gl`, val: hydration, set: setHydration, min: 0, max: 12, step: 1 },
              { label: `Consistency: ${consistency}%`, val: consistency, set: setConsistency, min: 0, max: 100, step: 5 },
            ].map((s) => (
              <div className="form-group" key={s.label}>
                <label className="form-label">{s.label}</label>
                <input
                  type="range" min={s.min} max={s.max} step={s.step}
                  value={s.val} onChange={(e) => s.set(Number(e.target.value))}
                />
              </div>
            ))}

            <div className="form-group">
              <label className="form-label">Workout Completed Today?</label>
              <div style={{ display: "flex", gap: "10px" }}>
                {[{ label: "✅ Yes", val: true }, { label: "❌ No", val: false }].map((v) => (
                  <button key={String(v.val)} onClick={() => setWorkout(v.val)}
                    className={`btn ${workout === v.val ? "btn-primary" : "btn-outline"}`}
                    style={{ flex: 1, justifyContent: "center" }}>
                    {v.label}
                  </button>
                ))}
              </div>
              {workout === null && (
                <p style={{ fontSize: "0.75rem", color: "var(--text-muted)", marginTop: "6px" }}>Please select an option above.</p>
              )}
            </div>

            <button
              className="btn btn-primary"
              style={{ width: "100%", justifyContent: "center", marginTop: "8px" }}
              onClick={runPrediction}
              disabled={loading || !canSubmit}
            >
              {loading ? "⏳ Analysing..." : "🔮 Run AI Prediction"}
            </button>

            {error && (
              <div className="alert alert-error" style={{ marginTop: "14px" }}>⚠️ {error}</div>
            )}
          </div>
        </Reveal>

        {/* Right Panel */}
        <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
          <Reveal direction="left" delay={80}>
            <div className="card corner-mark">
              <div className="bracket-title">Habit Metrics</div>
              <HabitTracker
                sleep={sleep} stress={stress} workout={workout}
                hydration={hydration} consistency={consistency}
              />
            </div>
          </Reveal>

          {prediction && (
            <Reveal direction="scale" delay={0}>
              <div className="card corner-mark" style={{ border: `1px solid ${riskColor}40` }}>
                <div className="bracket-title" style={{ color: riskColor }}>AI Prediction</div>
                <div style={{ textAlign: "center", marginBottom: "20px" }}>
                  <div style={{
                    fontFamily: "var(--font-display)", fontSize: "4.5rem", fontWeight: 900,
                    color: riskColor, lineHeight: 1, textShadow: `0 0 30px ${riskColor}60`,
                  }}>
                    {Math.round(prediction.skip_probability * 100)}%
                  </div>
                  <div style={{ fontSize: "0.78rem", color: "var(--text-muted)", marginTop: "6px", textTransform: "uppercase", letterSpacing: "1px" }}>
                    Skip Probability
                  </div>
                  <span className="badge" style={{
                    marginTop: "12px", display: "inline-block",
                    background: `${riskColor}18`, color: riskColor,
                    textTransform: "uppercase", fontSize: "0.75rem",
                  }}>
                    {prediction.risk} risk
                  </span>
                </div>
                <div className="progress-bar-wrap" style={{ marginBottom: "16px", height: "10px" }}>
                  <div className="progress-bar-fill"
                    style={{ width: `${prediction.skip_probability * 100}%`, background: riskColor }} />
                </div>
                <p style={{ fontSize: "0.875rem", color: "var(--text-secondary)", lineHeight: 1.7, textAlign: "center" }}>
                  {prediction.recommendation}
                </p>
              </div>
            </Reveal>
          )}

          {!prediction && !loading && (
            <div style={{ padding: "32px 24px", textAlign: "center", color: "var(--text-muted)", border: "1px dashed var(--border)", borderRadius: "var(--radius)" }}>
              <div style={{ fontSize: "2rem", marginBottom: "10px" }}>🔮</div>
              <div style={{ fontSize: "0.84rem" }}>Complete the form and run the prediction to see results.</div>
            </div>
          )}
        </div>
      </div>

      {/* Weekly Streak */}
      <Reveal direction="up" delay={100}>
        <div className="card corner-mark" style={{ marginTop: "28px" }}>
          <div className="bracket-title">Weekly Habit Streak</div>
          <p style={{ fontSize: "0.83rem", color: "var(--text-muted)", marginBottom: "20px" }}>
            Connect the backend to track your daily streak automatically.
          </p>
          <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
            {["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map((day) => (
              <div key={day} style={{
                flex: 1, minWidth: "70px",
                background: "var(--bg-primary)",
                border: "1px solid var(--border)",
                borderRadius: "var(--radius-sm)",
                padding: "16px 10px",
                textAlign: "center",
              }}>
                <div style={{ fontSize: "1.2rem", marginBottom: "6px" }}>⬜</div>
                <div style={{
                  fontFamily: "var(--font-display)", fontSize: "0.85rem", fontWeight: 700,
                  color: "var(--text-muted)", letterSpacing: "0.5px"
                }}>
                  {day}
                </div>
              </div>
            ))}
          </div>
        </div>
      </Reveal>
    </div>
  );
}

export default HabitPage;