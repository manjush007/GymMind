import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Filler, Tooltip, Legend);

const LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

function PerformanceChart({ stats }) {
  const perfData = stats?.weekly_performance || [];
  const caloriesData = stats?.weekly_calories || [];

  const hasData = perfData.length > 0 || caloriesData.length > 0;

  if (!hasData) {
    return (
      <div style={{
        height: "180px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        color: "var(--text-muted)",
        gap: "12px",
        border: "1px dashed rgba(255,255,255,0.07)",
        borderRadius: "var(--radius-sm)",
      }}>
        <div style={{ fontSize: "2rem" }}>📈</div>
        <div style={{ fontSize: "0.85rem", textAlign: "center" }}>
          No performance data yet.<br />Complete workouts to build your chart.
        </div>
      </div>
    );
  }

  const chartData = {
    labels: LABELS.slice(0, Math.max(perfData.length, caloriesData.length)),
    datasets: [
      {
        label: "Performance Score",
        data: perfData,
        borderColor: "#ff5722",
        backgroundColor: "rgba(255, 87, 34, 0.08)",
        fill: true,
        tension: 0.45,
        pointBackgroundColor: "#ff5722",
        pointBorderColor: "#08090e",
        pointBorderWidth: 2,
        pointRadius: 5,
        pointHoverRadius: 7,
      },
      {
        label: "Calories Burned",
        data: caloriesData,
        borderColor: "#2979ff",
        backgroundColor: "rgba(41, 121, 255, 0.07)",
        fill: true,
        tension: 0.45,
        pointBackgroundColor: "#2979ff",
        pointBorderColor: "#08090e",
        pointBorderWidth: 2,
        pointRadius: 5,
        pointHoverRadius: 7,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        labels: { color: "#7a869a", font: { family: "Inter", size: 12 }, usePointStyle: true, pointStyleWidth: 8 },
      },
      tooltip: {
        backgroundColor: "#10131c",
        borderColor: "rgba(255,87,34,0.2)",
        borderWidth: 1,
        titleColor: "#f0f2ff",
        bodyColor: "#7a869a",
        padding: 12,
        cornerRadius: 10,
      },
    },
    scales: {
      x: { grid: { color: "rgba(255,255,255,0.03)" }, ticks: { color: "#3e4a5e", font: { family: "Inter", size: 11 } } },
      y: { grid: { color: "rgba(255,255,255,0.03)" }, ticks: { color: "#3e4a5e", font: { family: "Inter", size: 11 } } },
    },
  };

  return (
    <div style={{ height: "280px", position: "relative" }}>
      <Line data={chartData} options={chartOptions} />
    </div>
  );
}

export default PerformanceChart;