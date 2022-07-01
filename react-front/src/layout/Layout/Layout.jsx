import styles from './Layout.module.css';
// import cn from 'classnames';
import { Header, Feedback, Footer } from '../../layout';
import React from 'react';

export const Layout = ({ children }) => {
  return <>
    <div className={styles.main}>
      <Header>
      </Header>
      <div className={styles.wrapper}>
        {children}
      </div>
      <Feedback/>
    </div>
    <Footer/>
  </>;
};

export const withLayout = (Component) => {
  return function withLayoutComponent ({ ...props }) {
    return (
      <Layout>
        <Component {...props}/>
      </Layout>
    );
  };
};
