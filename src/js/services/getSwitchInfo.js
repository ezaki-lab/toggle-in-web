import { generalToken as token } from './tokens';

const getSwitchInfo = (switchId) => {
  const url = `https://ezaki-lab.littlestar.jp/toggle-in-web/api/info/${switchId}`;

  return fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};

export default getSwitchInfo;
