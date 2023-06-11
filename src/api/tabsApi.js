import axios from 'axios'

export function getTabs() {
  return axios.get('/api/items/read/');
}

export function uploadTab(item) {
  return axios.post('/api/items/put/', item);
}

export function deleteTab(item) {
  return axios.post('/api/items/delete/', item);
}

export function uploadIcon(icon) {
  let form = new FormData();
  form.append("image", icon);
  return axios.post('/api/icons/', form);
}

