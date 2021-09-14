import React, { useEffect, useState } from 'react';
import addSwitch from '../services/addSwitch';
import getSwitchInfo from '../services/getSwitchInfo';
import switchToggle from '../services/switchToggle';
import updateUser from '../services/updateUser';

const Main = (props) => {
  const [inputName, setInputName] = useState('');
  const [toggles, setToggles] = useState([]);
  const [newSwitchName, setNewSwitchName] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    loadSwitches();
  }, [props.available]);

  const loadSwitches = async () => {
    const tmp = [];

    for (let toggle of props.available) {
      await getSwitchInfo(toggle)
        .then((res) => {
          if (res.status == 200 || res.status == 404) {
            return res.json();
          }
          throw new Error('Server Error');
        })
        .then((json) => {
          if (json.result === 'OK') {
            tmp.push({
              id: json.switch,
              status: json.status,
              token: json.token
            });
          }
        });
    }

    setToggles(tmp);
  };

  // リダイレクト
  const handlerButton = (e) => {
    window.location.href = `https://ezaki-lab.littlestar.jp/toggle-in-web/?user=${inputName}`;
  };

  const handlerAddSwitchClick = (e) => {
    addSwitch(newSwitchName)
      .then((res) => {
        if (res.status === 200 || res.status === 409) {
          return res.json();
        }
        throw new Error('Server Error');
      })
      .then((json) => {
        if (json.result === 'OK') {
          setMessage('登録しました。');
          (async () => {
            await updateUser(props.user, {
              'available': [
                ...props.available,
                newSwitchName
              ]
            }).then((res) => res.json()).then((json) => { console.log(json); });

            props.loadUser();
          })();
        } else {
          setMessage('そのIDは既に存在します');
        }
      });
  };

  return (
    <div
      className="p-10 min-h-full bg-yellow-200 border-white overflow-x-hidden"
      style={{ borderWidth: '24px' }}
    >
      {props.user !== 'unknown' ? (
        <>
          <h1 className="text-3xl text-green-900 font-bold">
            {props.user}さんようこそ！
          </h1>

          <ul>
            {toggles.map((toggle, index) =>
              <li
                className="my-5 bg-white rounded-xl overflow-hidden"
                key={toggle.id}
              >
                <div className="px-5 py-3 flex flex-row">
                  <h1 className="text-2xl font-medium flex flex-col justify-end">
                    {toggle.id}
                  </h1>

                  <div className="ml-10 flex flex-row">
                    {!toggle.status ? (
                      <>
                        <button
                          className="mr-5 px-5 py-2 font-medium bg-lime-500 rounded-2xl"
                          onClick={(e) => {
                            const tmp = [...toggles];
                            tmp[index].status = !tmp[index].status;
                            setToggles(tmp);

                            switchToggle(toggle.id);
                          }}
                        >
                          オン
                        </button>
                        <div
                          className="px-5 py-2 text-gray-700 font-medium bg-gray-300 rounded-2xl"
                        >
                          オフ
                        </div>
                      </>
                    ) : (
                      <>
                        <div
                          className="mr-5 px-5 py-2 text-gray-700 font-medium bg-gray-300 rounded-2xl"
                        >
                          オン
                        </div>
                        <button
                          className="px-5 py-2 font-medium bg-red-500 rounded-2xl"
                          onClick={(e) => {
                            const tmp = [...toggles];
                            tmp[index].status = !tmp[index].status;
                            setToggles(tmp);

                            switchToggle(toggle.id);
                          }}
                        >
                          オフ
                        </button>
                      </>
                    )}
                  </div>
                </div>

                <div className="p-5 bg-gray-100">
                  <div className="mb-2 border-b-2 pb-1 border-gray-300">
                    <span className="text-green-500 font-medium mr-5 pb-1">
                      GET
                    </span>
                    https://ezaki-lab.littlestar.jp/toggle-in-web/api/switch/{toggle.id}
                  </div>
                  <div>
                    <h1 className="font-medium">
                      Header
                    </h1>
                    <div className="ml-3 text-gray-800">
                      Authorization: Bearer {toggle.token}
                    </div>
                  </div>
                </div>
              </li>
            )}
            <li className="mt-5 flex flex-row">
              <h1 className="text-2xl font-medium flex flex-col justify-center">
                スイッチを追加
              </h1>
              <div className="ml-10 flex flex-col">
                <span className="text-sm">
                  スイッチID
                </span>
                <input
                  type="text"
                  value={newSwitchName}
                  onChange={(e) => {
                    setNewSwitchName(e.target.value.replace(/\s+/g, ""));
                  }}
                  className="w-64 px-3 py-1 rounded-xl border-2 border-yellow-500"
                />
              </div>
              <button
                className="px-3 py-1 ml-10 bg-yellow-200 font-medium border-2 border-yellow-600 rounded-xl"
                onClick={handlerAddSwitchClick}
              >
                追加
              </button>
            </li>
            <li>
              {message}
            </li>
          </ul>
        </>
      ) : (
        <div className="pt-32 flex flex-col items-center">
          <h1 className="mb-2 text-3xl font-bold">
            Who are you?
          </h1>
          名前を入力してください。

          <div className="mt-10 w-full flex flex-row">
            <input
              type="text"
              className="w-full px-3 py-1 rounded-xl"
              value={inputName}
              onChange={(e) => {
                setInputName(e.target.value);
              }}
            />
            <button
              className="px-3 py-1 ml-8 bg-yellow-200 font-medium border-2 border-yellow-600 rounded-xl"
              onClick={handlerButton}
            >
              GO
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Main;
