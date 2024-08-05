import axios from "axios"

export const Axiosinstance = axios.create({
    baseURL: "http://127.0.0.1:5000/prompts/dashboard"

})