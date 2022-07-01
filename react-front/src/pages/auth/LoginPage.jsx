import { withLayout } from '../../layout';
import { H } from '../../components';
import styles from './Auth.module.css';
import React, { FormEvent, useEffect, useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { useNavigate } from 'react-router-dom';
import { API, withBaseUrl } from '../../api';
import { fetchUserData } from '../../api/services';

const LoginPage = () => {
  const [token, setToken] = useState(null);
  const [{ isLoading, response, error }, doFetch] = useFetch(withBaseUrl(API.auth.create_jwt));
  const [isLoadingUser, setIsLoadingUser] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const body = {};
    const formData = new FormData(e.target);
    formData.forEach((value, key) => body[key] = value);
    doFetch({
      method: 'post',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ ...body })
    });
  };

  useEffect(() => {
    if (!response) {
      return;
    }
    localStorage.setItem('token', response?.access);
    navigate('/');
  }, [response]);

  return <>
    <H tag="h1">Login Page</H>
    <form method="POST" className={styles.form} onSubmit={(e) => handleSubmit(e)}>
      <input placeholder="email" name="email" type="email"/>
      <input placeholder="password" name="password" type="password"/>
      <button type="submit">Login</button>
    </form>
  </>;
};

export default withLayout(LoginPage);
