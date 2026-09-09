// calculate BMI
export function calculateBMI(weight, height) {
  const heightInMeters = height / 100;
  return (weight / (heightInMeters * heightInMeters)).toFixed(2);
}

// calculate workout score
export function calculateWorkoutScore(reps, targetReps) {
  if (!targetReps) return 0;
  return Math.min((reps / targetReps) * 100, 100);
}

// format date
export function formatDate(date) {
  const d = new Date(date);
  return d.toLocaleDateString();
}

// generate random workout performance data
export function generateMockPerformance() {
  return [60, 65, 70, 72, 80, 85, 90];
}