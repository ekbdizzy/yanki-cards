import {BodyProps} from "./Body.props";
import styles from './Body.module.css';
import cn from "classnames";


export const Body = ({children, ...props}: BodyProps): JSX.Element => {
    return <div className={cn(styles.body, {})} {...props}>{children}</div>;
};
