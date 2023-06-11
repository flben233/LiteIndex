import axios from "axios";

export function setPaste(text) {
    let data = new FormData();
    data.append("text", text);
    return axios.post("/api/paste", data);
}

export function getPaste() {
    return axios.get("/api/paste");
}