import {PProps} from "./P.props";
import styles from './P.module.css';
import cn from "classnames";


export const P = ({children, size = 'normal', color = 'purple', center = false, ...props}: PProps): JSX.Element => {
    return <p className={cn(styles.p, {
        [styles.normal]: size == 'normal',
        [styles.big]: size == 'big'
    }, {
        [styles.primary]: color == 'primary',
        [styles.cyan]: color == 'cyan',
        [styles.purple]: color == 'purple'
    }, {
        [styles.center]: center == true
    })} {...props}>
        {children}
    </p>;
};
