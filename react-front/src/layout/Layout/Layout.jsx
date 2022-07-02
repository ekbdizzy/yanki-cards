import styles from './Layout.module.scss';
import { Header, Footer, Body } from '../../layout';
import { TopMenu } from '../../components';
import React from 'react';

export const Layout = ({ children }) => {
  return <div className={styles.wrapper}>
    <Header>
      <TopMenu/>
    </Header>
    <Body>
      {children}
    </Body>
    <Footer/>
  </div>;
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
