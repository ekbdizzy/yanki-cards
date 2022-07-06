const baseUrl = `${process.env.REACT_APP_BASE_URL}/api/`;

const URLS = {
  about: '/about/',
  themes: '/themes/',
  interview: '/interview/',
  auth: {
    login: '/auth/login/',
    register: '/auth/register/',
  },
  profile: '/profile/',
  words: '/words/',

};

const API = {
  auth: {
    create_jwt: 'auth/jwt/create/',
    verify: 'auth/jwt/verify/',
    getUser: 'auth/users/me/',
  },
  translate: 'words/translate/',
};

const withBaseUrl = (url) => {
  return `${baseUrl}${url}`;
};

export { API, URLS, withBaseUrl };
