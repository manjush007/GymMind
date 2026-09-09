import API from "./api";

export const getHabitPrediction = async (data) => {
  const res = await API.post("/habit/predict", data);
  return res.data;
};