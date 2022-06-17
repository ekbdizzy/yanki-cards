import {SidebarProps} from "./Sidebar.props";
import styles from './Sidebar.module.css';
import cn from 'classnames';

export const Sidebar = ({children, ...props}: SidebarProps): JSX.Element => {
    return <aside className={cn(styles.sidebar, {})}
                  {...props}>
        {children}
        sidebar
    </aside>;
};
