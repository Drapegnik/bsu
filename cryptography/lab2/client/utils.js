export const api = {
  login: 'login',
  getData: 'data',
  private: {
    rsaGenerate: 'private/rsa/generate',
    rsaDecrypt: 'private/rsa/decrypt',
    aesDecrypt: 'private/aes/decrypt',
  },
};

export const post = async (url, data) => {
  const response = await fetch(`http://localhost:5000/${url}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  const { status } = response;
  const json = await response.json();
  if (status !== 200) {
    const { error } = json;
    throw { status, error };
  }
  return json.data;
};
