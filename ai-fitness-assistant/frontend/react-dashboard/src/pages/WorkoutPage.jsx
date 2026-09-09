import { useState, useEffect, useRef } from "react";
import WorkoutCard from "../components/WorkoutCard";
import { Reveal } from "../utils/useScrollReveal";
import { getWorkoutStats, getWorkoutHistory } from "../services/workoutService";

const categories = ["All", "Chest", "Back", "Legs", "Shoulders", "Core"];

function AnimatedWorkoutCard({ workout, index }) {
  const ref = useRef(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.style.opacity = "0";
    el.style.transform = "translateY(32px) scale(0.95)";
    el.style.transition = `opacity 0.55s cubic-bezier(0.22,1,0.36,1) ${index * 0.08}s,
                           transform 0.55s cubic-bezier(0.22,1,0.36,1) ${index * 0.08}s`;
    const obs = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        el.style.opacity = "1";
        el.style.transform = "translateY(0) scale(1)";
        obs.unobserve(el);
      }
    }, { threshold: 0.08 });
    obs.observe(el);
    return () => obs.disconnect();
  }, [index]);
  return <div ref={ref}><WorkoutCard {...workout} /></div>;
}

function EmptyState({ icon = "📭", message, sub }) {
  return (
    <div style={{ padding: "48px 0", textAlign: "center", color: "var(--text-muted)" }}>
      <div style={{ fontSize: "2.5rem", marginBottom: "14px" }}>{icon}</div>
      <div style={{ fontFamily: "var(--font-display)", fontSize: "1rem", fontWeight: 700, color: "var(--text-secondary)", textTransform: "uppercase", letterSpacing: "0.5px", marginBottom: "6px" }}>{message}</div>
      {sub && <div style={{ fontSize: "0.82rem" }}>{sub}</div>}
    </div>
  );
}

function WorkoutPage() {
  const [filter, setFilter] = useState("All");
  const [workouts, setWorkouts] = useState([]);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.allSettled([
      getWorkoutHistory(),
      getWorkoutStats(),
    ]).then(([histResult, statsResult]) => {
      if (histResult.status === "fulfilled") setWorkouts(histResult.value || []);
      if (statsResult.status === "fulfilled") setSummary(statsResult.value);
    }).finally(() => setLoading(false));
  }, []);

  const filtered = filter === "All"
    ? workouts
    : workouts.filter((w) => w.category === filter);

  return (
    <div className="page-container">

      <Reveal direction="up">
        <div className="accent-line" />
        <h1 className="hero-title">Workout Tracker 💪</h1>
        <div className="page-subtitle">Track and manage your exercise sessions</div>
      </Reveal>

      {/* AI Camera Banner */}
      <Reveal direction="up" delay={100}>
        <div style={{
          background: "linear-gradient(135deg, rgba(255,87,34,0.08), rgba(41,121,255,0.06))",
          border: "1px solid rgba(255,87,34,0.18)",
          borderRadius: "var(--radius)", padding: "20px 24px", marginBottom: "32px",
          display: "flex", alignItems: "center", gap: "20px",
        }}>
          <div style={{ fontSize: "2.5rem" }}>📷</div>
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: "var(--font-display)", fontWeight: 800, fontSize: "1.1rem", color: "var(--text-primary)", textTransform: "uppercase", letterSpacing: "0.5px", marginBottom: "4px" }}>
              AI Pose Detection
            </div>
            <div style={{ fontSize: "0.85rem", color: "var(--text-secondary)" }}>
              Real-time AI-powered form analysis. Connect your webcam for posture feedback.
            </div>
          </div>
          <button className="btn btn-primary border-trace" style={{ whiteSpace: "nowrap" }}>
            🎥 Start Camera
          </button>
        </div>
      </Reveal>

      {/* Category Filter */}
      <Reveal direction="right" delay={50}>
        <div style={{ display: "flex", gap: "10px", marginBottom: "28px", flexWrap: "wrap" }}>
          {categories.map((cat) => (
            <button key={cat}
              className={`btn ${filter === cat ? "btn-primary" : "btn-outline"}`}
              style={{ padding: "8px 18px", fontSize: "0.85rem" }}
              onClick={() => setFilter(cat)}
            >{cat}</button>
          ))}
        </div>
      </Reveal>

      {/* Workout Cards */}
      {loading ? (
        <EmptyState icon="⏳" message="Loading workouts..." />
      ) : filtered.length === 0 ? (
        <EmptyState icon="🏋️" message="No workouts found"
          sub={filter === "All" ? "Complete a workout session to see it here." : `No ${filter} workouts logged yet.`} />
      ) : (
        <div className="workout-cards-grid">
          {filtered.map((w, i) => (
            <AnimatedWorkoutCard key={`${filter}-${i}`} workout={w} index={i} />
          ))}
        </div>
      )}

      {/* Today's Summary */}
      <Reveal direction="up" delay={120}>
        <div className="card corner-mark" style={{ marginTop: "32px" }}>
          <div className="bracket-title">Today's Summary</div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "20px", textAlign: "center" }}>
            {[
              { label: "Exercises Done", value: summary?.today_exercises ?? "--", icon: "✅" },
              { label: "Total Reps", value: summary?.today_reps ?? "--", icon: "🔁" },
              { label: "Calories", value: summary?.today_calories ? `${summary.today_calories} kcal` : "--", icon: "🔥" },
            ].map((s) => (
              <div key={s.label} style={{
                background: "var(--bg-primary)", borderRadius: "var(--radius-sm)",
                padding: "20px", border: "1px solid var(--border)",
              }}>
                <div style={{ fontSize: "1.8rem", marginBottom: "8px" }}>{s.icon}</div>
                <div style={{ fontFamily: "var(--font-display)", fontSize: "1.6rem", fontWeight: 900, color: "var(--orange)" }}>{s.value}</div>
                <div style={{ fontSize: "0.78rem", color: "var(--text-muted)", marginTop: "4px", textTransform: "uppercase", letterSpacing: "0.8px" }}>{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </Reveal>
    </div>
  );
}

export default WorkoutPage;