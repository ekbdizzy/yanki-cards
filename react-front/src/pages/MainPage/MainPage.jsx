import { withLayout } from '../../layout';
import { H } from '../../components';
import React, { useEffect} from 'react';
import { API, withBaseUrl } from '../../api';

const MainPage = () => {
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      return;
    }

    const fetchUserData = async (token) => {
      const response = await fetch(withBaseUrl(API.auth.getUser),
        {
          headers: new Headers({
            'Content-type': 'application/json',
            Authorization: `Bearer ${token}`
          })
        });

      return <>
        <H tag="h1">Main Page</H>
      </>;
    };
  });
};

export default withLayout(MainPage);
