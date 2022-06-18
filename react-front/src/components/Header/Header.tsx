import {HeaderProps} from "./Header.props";
import styles from './Header.module.css';
import cn from 'classnames';

export const Header = ({tag = 'h1', children, ...props}: HeaderProps): JSX.Element => {
    switch (tag) {
        case 'h1':
            return <h1 className={cn(styles.header, styles.h1)} {...props}>{children}</h1>;
        case 'h2':
            return <h2 className={cn(styles.header, styles.h2)} {...props}>{children}</h2>;
        default:
            return <></>;
    }
};
