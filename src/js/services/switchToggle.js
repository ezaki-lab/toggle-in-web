import { generalToken as token } from './tokens';

const switchToggle = (switchId) => {
  const url = `https://ezaki-lab.littlestar.jp/toggle-in-web/api/switch/${switchId}`;

  return fetch(url, {
    method: 'PUT',
    cache: 'no-cache',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};

export default switchToggle;
