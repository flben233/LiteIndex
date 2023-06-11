import axios from "axios";

export function login(username, password) {
    let data = new FormData();
    data.append("username", username);
    data.append("password", password);
    return axios.post("/api/login", data);
}