export const api = {
  login: 'login',
  getData: 'data',
  private: {
    rsaGenerate: 'private/rsa/generate',
    rsaDecrypt: 'private/rsa/decrypt',
    aesDecrypt: 'private/aes/decrypt',
  },
};

export const post = (url, data) =>
  fetch(`http://localhost:5000/${url}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(({ data, error }) => {
      if (error) {
        throw error;
      }
      return data;
    });
