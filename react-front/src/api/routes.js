const baseUrl = `${process.env.REACT_APP_BASE_URL}/api/`;

const API = {
  auth: {
    create_jwt: 'auth/jwt/create/',
    verify: 'auth/jwt/verify/',
    getUser: 'auth/users/me/',
  },
};

const withBaseUrl = (url) => {
  return `${baseUrl}${url}`;
};

export { API, withBaseUrl };
