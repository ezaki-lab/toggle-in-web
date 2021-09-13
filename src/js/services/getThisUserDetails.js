import { generalToken as token } from './tokens';

// そのユーザーの情報を取得する
const getThisUserDetails = (username) => {
  const url = `https://ezaki-lab.littlestar.jp/toggle-in-web/api/user/${username}`;

  return fetch(url, {
    method: 'GET',
    cache: 'no-cache',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
};

export default getThisUserDetails;
