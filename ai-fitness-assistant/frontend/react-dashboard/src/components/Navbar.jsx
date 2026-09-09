import { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";

const navLinks = [
  { to: "/", label: "Dashboard", icon: "🏠" },
  { to: "/workout", label: "Workouts", icon: "💪" },
  { to: "/diet", label: "Diet", icon: "🥗" },
  { to: "/habit", label: "Habits", icon: "📊" },
];

function Navbar() {
  const location = useLocation();
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handler = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", handler);
    return () => window.removeEventListener("scroll", handler);
  }, []);

  return (
    <nav style={{
      position: "fixed",
      top: 0, left: 0, right: 0,
      height: "64px",
      background: "#ffffff",
      backdropFilter: "blur(10px)",
      borderBottom: "1px solid #e0e3e8",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      padding: "0 32px",
      zIndex: 900,
      boxShadow: scrolled ? "0 2px 8px rgba(0, 0, 0, 0.08)" : "none",
      transition: "box-shadow 0.3s ease",
    }}>

      {/* Logo */}
      <Link to="/" style={{ textDecoration: "none", display: "flex", alignItems: "center", gap: "12px" }}>
        <div style={{
          width: "40px", height: "40px",
          background: "linear-gradient(135deg, #2e8b57, #4caf50)",
          borderRadius: "10px",
          display: "flex", alignItems: "center", justifyContent: "center",
          fontSize: "1.2rem",
          fontWeight: 700,
          color: "#fff",
        }}>❤️</div>
        <div>
          <div style={{
            fontFamily: "'Plus Jakarta Sans', sans-serif",
            fontSize: "1.15rem",
            fontWeight: 700,
            color: "#212529",
            letterSpacing: "-0.3px",
            lineHeight: 1,
          }}>FitAI</div>
          <div style={{ fontSize: "0.65rem", color: "#999999", letterSpacing: "0.3px", fontWeight: 500 }}>
            Health Coach
          </div>
        </div>
      </Link>

      {/* Nav Links */}
      <div style={{ display: "flex", alignItems: "center", gap: "4px" }}>
        {navLinks.map((link) => {
          const active = location.pathname === link.to;
          return (
            <Link
              key={link.to}
              to={link.to}
              style={{
                display: "flex",
                alignItems: "center",
                gap: "6px",
                padding: "8px 16px",
                borderRadius: "8px",
                textDecoration: "none",
                fontFamily: "'Plus Jakarta Sans', sans-serif",
                fontSize: "0.9rem",
                fontWeight: active ? 700 : 600,
                letterSpacing: "-0.2px",
                textTransform: "none",
                color: active ? "#2e8b57" : "#666666",
                background: active ? "rgba(46, 139, 87, 0.08)" : "transparent",
                border: active ? "1px solid rgba(46, 139, 87, 0.2)" : "1px solid transparent",
                boxShadow: active ? "none" : "none",
                transition: "all 0.2s ease",
              }}
            >
              <span style={{ fontSize: "0.9rem" }}>{link.icon}</span>
              {link.label}
            </Link>
          );
        })}
      </div>

      {/* User Avatar */}
      <div style={{
        width: "40px", height: "40px",
        borderRadius: "10px",
        background: "linear-gradient(135deg, #0097a7, #1976d2)",
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: "0.9rem",
        fontWeight: 700,
        color: "#fff",
        cursor: "pointer",
        fontFamily: "'Plus Jakarta Sans', sans-serif",
        letterSpacing: "0px",
      }}>
        U
      </div>
    </nav>
  );
}

export default Navbar;