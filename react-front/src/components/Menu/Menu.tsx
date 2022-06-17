import {MenuProps} from "./Menu.props";
import styles from "./Menu.module.css";
import cn from 'classnames';


export const Menu = ({children, ...props}: MenuProps): JSX.Element => {
    return <ul className={cn(styles.menu, {

    })}
        {...props}>
        {children}
    </ul>;
};
