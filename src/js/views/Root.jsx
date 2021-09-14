import React, { useEffect, useRef, useState } from 'react';
import getThisUserDetails from '../services/getThisUserDetails';
import Main from './Main';

const Root = () => {
  const [user, setUser] = useState('');
  const [available, setAvailable] = useState([]);

  const mainObj = useRef(null);

  // ロード時とリサイズ時に、ウィンドウサイズを最大にする
  useEffect(() => {
    window.addEventListener('load', () => {
      changeWindowSize();
    });
    window.addEventListener('resize', () => {
      changeWindowSize();
    });
  }, []);

  // URL変数「user」にユーザーが指定されていたら、そのユーザーのページを表示
  useEffect(() => {
    loadUser();
  }, []);

  const loadUser = () => {
    const url = new URL(location.href);
    const userByUrl = url.searchParams.get("user");

    if (userByUrl !== null) {
      setUser(userByUrl);

      getThisUserDetails(userByUrl)
        .then((res) => {
          if (res.status === 200 || res.status === 404) {
            return res.json();
          }
          throw new Error('Server Error');
        })
        .then((json) => {
          setAvailable(json.available);
        });
    } else {
      setUser('unknown');
    }
  };

  // main要素のサイズを最大に
  const changeWindowSize = () => {
    mainObj.current.style.width = `${window.innerWidth}px`;
    mainObj.current.style.height = `${window.innerHeight}px`;
  };

  return (
    <main
      ref={mainObj}
    >
      <Main
        user={user}
        available={available}
        loadUser={loadUser}
      />
    </main>
  );
};

export default Root;
