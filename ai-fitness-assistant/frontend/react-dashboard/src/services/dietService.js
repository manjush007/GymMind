import API from "./api";

export const getDietPlan = async (data) => {
  const res = await API.post("/diet/generate", data);
  return res.data;
};  