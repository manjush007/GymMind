import API from "./api";

export const getWorkoutStats = async () => {
  const res = await API.get("/workout/stats");
  return res.data;
};

export const getWorkoutHistory = async () => {
  const res = await API.get("/workout/history");
  return res.data;
};