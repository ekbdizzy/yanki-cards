import {HeaderProps} from "./Header.props";
import styles from "./Header.module.css";
import cn from 'classnames';

export const Header = ({children, ...props}: HeaderProps): JSX.Element => {
    return <header className={cn(styles.header, {})}
                   {...props}>
        {children}
        header
    </header>;
};
