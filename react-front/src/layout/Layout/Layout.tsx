import {LayoutProps} from "./Layout.props";
import styles from './Layout.module.css';
import cn from 'classnames';
import {Header} from "../Header/Header";
import {Feedback} from "../Feedback/Feedback";
import {Footer} from "../Footer/Footer";
import {Sidebar} from "../Sidebar/Sidebar";
import {FunctionComponent} from "react";

export const Layout = ({children}: LayoutProps): JSX.Element => {
    return <>
        <Header/>
        <div>
            <Sidebar/>
            <div>{children}</div>
            <Feedback/>
        </div>
        <Footer/>
    </>;
};

export const withLayout = <T extends Record<string, unknown>>(Component: FunctionComponent<T>) => {
    return function withLayoutComponent({...props}: T): JSX.Element {
        return (
            <Layout>
                <Component {...props}/>
            </Layout>
        );
    };
};
