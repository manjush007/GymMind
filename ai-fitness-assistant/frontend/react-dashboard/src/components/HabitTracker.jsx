function HabitTracker({ sleep, stress, workout, consistency, hydration }) {
  const metrics = [
    {
      label: "Sleep Hours",
      icon: "😴",
      value: sleep,
      unit: "hrs",
      max: 10,
      color: "#2979ff",   // blue
      good: sleep >= 7,
    },
    {
      label: "Stress Level",
      icon: "😤",
      value: stress,
      unit: "/10",
      max: 10,
      color: "#f44336",   // red
      good: stress <= 4,
    },
    {
      label: "Workout Consistency",
      icon: "💪",
      value: consistency || (workout ? 80 : 30),
      unit: "%",
      max: 100,
      color: "#ff5722",   // orange
      good: (consistency || 0) >= 70 || workout,
    },
    {
      label: "Hydration",
      icon: "💧",
      value: hydration || 6,
      unit: "glasses",
      max: 8,
      color: "#448aff",   // light blue
      good: (hydration || 0) >= 6,
    },
  ];

  return (
    <div>
      {metrics.map((m) => (
        <div key={m.label} className="habit-metric">
          <div className="habit-metric-header">
            <div className="habit-metric-label">
              <span>{m.icon}</span>
              {m.label}
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
              <span className="habit-metric-value">
                {m.value}{m.unit}
              </span>
              <span className={`badge ${m.good ? "badge-orange" : "badge-red"}`}>
                {m.good ? "Good" : "Low"}
              </span>
            </div>
          </div>
          <div className="progress-bar-wrap">
            <div
              className="progress-bar-fill"
              style={{
                width: `${Math.min((m.value / m.max) * 100, 100)}%`,
                background: m.color,
              }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}

export default HabitTracker;