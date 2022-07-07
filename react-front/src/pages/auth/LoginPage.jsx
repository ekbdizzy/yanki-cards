import { withLayout } from '../../layout';
// import styles from './Auth.module.css';
import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Htag } from '../../components';
// import { useNavigate } from 'react-router-dom';
// import { API, withBaseUrl } from '../../api';
import { Auth } from './Auth';

const LoginPage = () => {
  return (
    <Auth title='Login'/>
  );
};

export default withLayout(LoginPage);
