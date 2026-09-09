function WorkoutCard({ exercise, reps, calories, icon, category, duration }) {
  return (
    <div className="workout-card angled-card corner-mark">
      <div className="workout-card-content">
        {/* Ghost jersey-style number (reps) */}
        <div className="jersey-number" style={{ fontSize: "4.5rem", top: "8px", right: "10px" }}>{reps}</div>

        <div className="workout-icon">{icon || "🏋️"}</div>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div>
            <div className="workout-name">{exercise}</div>
            <span className="sport-tag" style={{ marginTop: "6px", display: "inline-flex", fontSize: "0.68rem", padding: "3px 9px" }}>
              {category || "Strength"}
            </span>
          </div>
        </div>
        <div className="workout-meta">
          <span>🔁 {reps} reps</span>
          <span>🔥 {calories} kcal</span>
          {duration && <span>⏱ {duration}m</span>}
        </div>

        {/* Progress bar */}
        <div style={{ marginTop: "16px" }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "6px" }}>
            <span style={{ fontSize: "0.72rem", color: "var(--text-muted)", textTransform: "uppercase", letterSpacing: "0.8px" }}>Progress</span>
            <span style={{ fontSize: "0.72rem", color: "var(--orange)", fontWeight: 700 }}>
              {Math.round((reps / 15) * 100)}%
            </span>
          </div>
          <div className="progress-bar-wrap">
            <div
              className="progress-bar-fill"
              style={{
                width: `${Math.min((reps / 15) * 100, 100)}%`,
                background: "linear-gradient(90deg, var(--orange), var(--blue))",
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default WorkoutCard;