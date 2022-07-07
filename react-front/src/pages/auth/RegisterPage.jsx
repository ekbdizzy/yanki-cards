import { withLayout } from '../../layout';
import React from 'react';
import { Auth } from './Auth';

const RegisterPage = () => {
  return (
    <Auth title="Sign Up"/>
  );
};

export default withLayout(RegisterPage);
