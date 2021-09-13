import React, { useEffect, useRef, useState } from 'react';
import getThisUserDetails from '../services/getThisUserDetails';

const Root = () => {
  const [user, setUser] = useState('unknown');

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
    const url = new URL(location.href);
    const userByUrl = url.searchParams.get("user");

    getThisUserDetails(userByUrl)
      .then((res) => {
        if (res.status === 200 || res.status === 404) {
          return res.json();
        }
        throw new Error('Server Error');
      })
      .then((json) => {
        if (json.result !== 'Not Found') {
          setUser(json.user);
          console.log(json.available);
        }
      });
  });

  // main要素のサイズを最大に
  const changeWindowSize = () => {
    mainObj.current.style.width = `${window.innerWidth}px`;
    mainObj.current.style.height = `${window.innerHeight}px`;
  };

  return (
    <div
      className={className}
      ref={mainObj}
    >
      <h1>Hello {user}</h1>
    </div>
  );
};

export default Root;
