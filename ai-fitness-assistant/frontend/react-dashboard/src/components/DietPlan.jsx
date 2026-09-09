function DietPlan({ calories, protein, carbs, fat, meals, goal }) {
  const macros = [
    { label: "Calories", value: `${calories} kcal`, color: "#7c4dff", pct: 100 },
    { label: "Protein", value: `${protein}g`, color: "#00e676", pct: Math.min((protein / 200) * 100, 100) },
    { label: "Carbohydrates", value: `${carbs || 0}g`, color: "#448aff", pct: Math.min((carbs / 300) * 100, 100) },
    { label: "Fats", value: `${fat || 0}g`, color: "#ff6d00", pct: Math.min((fat / 100) * 100, 100) },
  ];

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
      {/* Goal Banner */}
      {goal && (
        <div style={{
          padding: "14px 18px",
          borderRadius: "10px",
          background: "rgba(124, 77, 255, 0.1)",
          border: "1px solid rgba(124, 77, 255, 0.25)",
          display: "flex",
          alignItems: "center",
          gap: "10px",
        }}>
          <span style={{ fontSize: "1.3rem" }}>🎯</span>
          <div>
            <div style={{ fontSize: "0.8rem", color: "var(--text-muted)", textTransform: "uppercase", letterSpacing: "0.6px" }}>
              Goal
            </div>
            <div style={{ fontSize: "0.95rem", fontWeight: 700, color: "var(--accent-purple)", textTransform: "capitalize" }}>
              {goal}
            </div>
          </div>
        </div>
      )}

      {/* Macro Grid */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: "14px" }}>
        {macros.map((m) => (
          <div key={m.label} style={{
            background: "var(--bg-primary)",
            borderRadius: "10px",
            padding: "16px",
            border: "1px solid var(--border)",
          }}>
            <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", marginBottom: "6px" }}>{m.label}</div>
            <div style={{ fontSize: "1.3rem", fontWeight: 800, color: m.color, marginBottom: "8px" }}>{m.value}</div>
            <div className="progress-bar-wrap">
              <div className="progress-bar-fill" style={{ width: `${m.pct}%`, background: m.color }} />
            </div>
          </div>
        ))}
      </div>

      {/* Meal List */}
      {meals && meals.length > 0 && (
        <div>
          <div className="section-title">
            <span className="dot" />
            Suggested Meals
          </div>
          {meals.map((meal, idx) => (
            <div key={idx} className="meal-item">
              <div className="meal-icon">{meal.icon || "🍽️"}</div>
              <div className="meal-details">
                <div className="meal-name">{typeof meal === "string" ? meal : meal.name}</div>
                {meal.time && <div className="meal-macro">{meal.time} · {meal.cal || ""}</div>}
              </div>
              {meal.cal && (
                <span className="badge badge-green">{meal.cal}</span>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default DietPlan;