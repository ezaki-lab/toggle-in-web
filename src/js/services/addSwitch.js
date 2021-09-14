import { generalToken as token } from './tokens';

const addSwitch = (switchId) => {
  const url = `https://ezaki-lab.littlestar.jp/toggle-in-web/api/switch/${switchId}`;

  return fetch(url, {
    method: 'POST',
    cache: 'no-cache',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};

export default addSwitch;
