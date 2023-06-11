import axios from "axios";

export function uploadWallpaper(wallpaper) {
  let form = new FormData();
  form.append("image", wallpaper);
  return axios.post('/api/images/wallpaper/', form);
}

export function getPerformanceInfo() {
  return axios.get('/api/performance/');
}
