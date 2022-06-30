import {LayoutProps} from "./Layout.props";
import styles from './Layout.module.css';
import cn from 'classnames';
import {Menu} from "../../components";
import {Header, Body, Feedback, Footer} from '../../layout';
import React, {FunctionComponent} from "react";

import {CurrentUserContextProvider, IUserContext} from "../../context/currentUser";

export const Layout = ({children}: LayoutProps): JSX.Element => {
    return <>
        <div className={styles.main}>
            <Header>
                <Menu/>
            </Header>
            <div className={styles.wrapper}>
                {children}

            </div>
            <Feedback/>

        </div>
        <Footer/>
    </>;
};

export const withLayout = <T extends Record<string, unknown> & IUserContext>(Component: FunctionComponent<T>) => {
    return function withLayoutComponent({...props}: T): JSX.Element {
        return (

                <Layout>
                    <Component {...props}/>
                </Layout>
        );
    };
};
