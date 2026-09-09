import { useState, useEffect, useRef } from "react";
import PerformanceChart from "../components/PerformanceChart";
import { Reveal } from "../utils/useScrollReveal";
import { getWorkoutStats } from "../services/workoutService";

function AnimatedStatCard({ label, value, unit, icon, color, change, jerseyNum, loading }) {
  const ref = useRef(null);
  const index = { blue: 0, orange: 1, gold: 2, red: 3 }[color] ?? 0;

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.style.opacity = "0";
    el.style.transform = "translateY(40px)";
    el.style.transition = `opacity 0.65s cubic-bezier(0.22,1,0.36,1) ${index * 0.1}s,
                           transform 0.65s cubic-bezier(0.22,1,0.36,1) ${index * 0.1}s`;
    const obs = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        el.style.opacity = "1";
        el.style.transform = "translateY(0)";
        obs.unobserve(el);
      }
    }, { threshold: 0.1 });
    obs.observe(el);
    return () => obs.disconnect();
  }, [index]);

  return (
    <div ref={ref} className={`stat-card ${color} corner-mark angled-card`}
      style={{ position: "relative", overflow: "hidden" }}>
      <div className="jersey-number">{jerseyNum ?? "--"}</div>
      <div style={{ position: "relative", zIndex: 1 }}>
        <div className="stat-icon">{icon}</div>
        <div className="stat-label">{label}</div>
        <div className="stat-value">
          {loading ? "--" : (value ?? "--")}
          <span className="stat-unit">{unit}</span>
        </div>
        {change && !loading && (
          <div className="stat-change">↑ {change}</div>
        )}
      </div>
    </div>
  );
}

function EmptyRow({ message }) {
  return (
    <div style={{ padding: "32px 0", textAlign: "center", color: "var(--text-muted)" }}>
      <div style={{ fontSize: "1.8rem", marginBottom: "10px" }}>📭</div>
      <div style={{ fontSize: "0.85rem" }}>{message}</div>
    </div>
  );
}

function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [recentWorkouts, setRecent] = useState([]);

  useEffect(() => {
    getWorkoutStats()
      .then((data) => setStats(data))
      .catch(() => setStats(null))
      .finally(() => setLoading(false));
  }, []);

  const statCards = [
    { label: "Total Workouts", value: stats?.total_workouts, jerseyNum: stats?.total_workouts ?? "--", unit: "sessions", icon: "🏋️", color: "blue", change: stats?.weekly_change },
    { label: "Calories Burned", value: stats?.calories_burned, jerseyNum: stats?.calories_burned ?? "--", unit: "kcal", icon: "🔥", color: "orange", change: stats?.calories_change },
    { label: "Avg Performance", value: stats?.avg_performance, jerseyNum: stats?.avg_performance ?? "--", unit: "/ 100", icon: "⚡", color: "gold", change: stats?.performance_change },
    { label: "Streak", value: stats?.streak_days, jerseyNum: stats?.streak_days ?? "--", unit: "days", icon: "🎯", color: "red", change: stats?.streak_label },
  ];

  return (
    <div className="page-container">

      {/* Hero Banner */}
      <Reveal direction="up">
        <div className="hero-strip sport-stripes" style={{ marginBottom: "32px" }}>
          <div className="speed-lines">
            <span /><span /><span /><span />
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", flexWrap: "wrap", gap: "16px" }}>
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "12px" }}>
                <span className="live-dot" />
                <span style={{ fontSize: "0.72rem", fontWeight: 700, color: "var(--orange)", textTransform: "uppercase", letterSpacing: "1.5px" }}>
                  Live Dashboard
                </span>
              </div>
              <div className="accent-line" />
              <h1 className="hero-title">Fitness Dashboard</h1>
              <div className="page-subtitle" style={{ marginBottom: 0 }}>
                Connect your backend to see real-time data
              </div>
            </div>
            <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
              <span className="sport-tag">🏆 Overview</span>
              <span className="sport-tag blue">� API Ready</span>
            </div>
          </div>
        </div>
      </Reveal>

      {/* Stat Cards */}
      <div className="stats-grid">
        {statCards.map((s) => (
          <AnimatedStatCard key={s.label} {...s} loading={loading} />
        ))}
      </div>

      <div className="sport-divider"><span className="sport-divider-icon">⚡</span></div>

      {/* Performance Chart */}
      <Reveal direction="up" delay={80}>
        <div className="card corner-mark" style={{ marginBottom: "24px" }}>
          <div className="bracket-title">Weekly Performance</div>
          <PerformanceChart stats={stats} />
        </div>
      </Reveal>

      {/* Bottom Grid */}
      <div className="grid-2">

        {/* Recent Workouts */}
        <Reveal direction="right">
          <div className="card corner-mark">
            <div className="bracket-title">Recent Workouts</div>
            {loading ? (
              <EmptyRow message="Loading workout history..." />
            ) : recentWorkouts.length === 0 ? (
              <EmptyRow message="No recent workouts. Start your first session!" />
            ) : (
              recentWorkouts.map((w, i) => (
                <div key={i} style={{
                  display: "flex", justifyContent: "space-between", alignItems: "center",
                  padding: "12px 0",
                  borderBottom: i < recentWorkouts.length - 1 ? "1px solid rgba(255,255,255,0.04)" : "none",
                }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
                    <div style={{ width: "4px", height: "38px", background: "linear-gradient(180deg,var(--orange),var(--blue))", borderRadius: "2px" }} />
                    <div>
                      <div style={{ fontWeight: 700, color: "var(--text-primary)", fontSize: "0.9rem" }}>{w.name}</div>
                      <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", marginTop: "2px" }}>{w.date} · {w.duration}</div>
                    </div>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <div style={{ fontFamily: "var(--font-display)", fontSize: "1.5rem", fontWeight: 900, color: "var(--orange)", lineHeight: 1 }}>{w.score}</div>
                    <div style={{ fontSize: "0.65rem", color: "var(--text-muted)", textTransform: "uppercase" }}>pts</div>
                  </div>
                </div>
              ))
            )}
          </div>
        </Reveal>

        {/* AI Insights */}
        <Reveal direction="left" delay={100}>
          <div className="card sport-stripes corner-mark">
            <div className="bracket-title">AI Insights</div>
            {stats?.insights && stats.insights.length > 0 ? (
              stats.insights.map((t, i) => (
                <div key={i} style={{
                  display: "flex", gap: "12px", padding: "12px 0",
                  borderBottom: i < stats.insights.length - 1 ? "1px solid rgba(255,255,255,0.04)" : "none",
                  alignItems: "flex-start",
                }}>
                  <div style={{
                    width: "32px", height: "32px", borderRadius: "8px",
                    background: "rgba(255,87,34,0.1)", border: "1px solid rgba(255,87,34,0.25)",
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: "1rem", flexShrink: 0,
                  }}>💡</div>
                  <p style={{ fontSize: "0.84rem", color: "var(--text-secondary)", lineHeight: 1.6 }}>{t}</p>
                </div>
              ))
            ) : (
              <EmptyRow message="AI insights will appear once your backend is connected and you have workout history." />
            )}
          </div>
        </Reveal>
      </div>
    </div>
  );
}

export default Dashboard;