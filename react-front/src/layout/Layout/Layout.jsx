import styles from './Layout.module.scss';
import { Header, Footer, Body } from '../../layout';
import { TopMenu } from '../../components';
import React from 'react';

export const Layout = ({ children }) => {
  return <>
    <div className={styles.layout}>

      <div className={styles.wrapper}>
        <Header>
          <TopMenu/>
        </Header>
      </div>

      <div className={styles.wrapper}>
        <Body>
          {children}
        </Body>
      </div>
      <Footer/>
    </div>
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
