import { generalToken as token } from './tokens';

// そのユーザーの情報を更新する
const updateUser = (username, info) => {
  const url = `https://ezaki-lab.littlestar.jp/toggle-in-web/api/user/${username}`;

  return fetch(url, {
    method: 'PUT',
    cache: 'no-cache',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(info)
  });
};

export default updateUser;
