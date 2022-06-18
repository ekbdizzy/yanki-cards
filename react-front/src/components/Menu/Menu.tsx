import {MenuItem, MenuProps} from "./Menu.props";
import styles from "./Menu.module.css";
import cn from 'classnames';
import {Link} from 'react-router-dom';

export const Menu = ({...props}: MenuProps): JSX.Element => {

    const menuItems: MenuItem[] = [
        {name: "Main", route: '/'},
        {name: "About", route: '/about'},
        {name: "Interview", route: '/Interview'},
        {name: "Profile", route: '/profile'},
        {name: "My words", route: '/words'}
    ];

    const buildMenu = (menuItems: MenuItem[]): JSX.Element => {
        return <ul className={cn(styles.menu)} {...props}>
            {menuItems.map(item => {
                return <li className={cn(styles.menu_item)} key={item.route}>
                    <Link to={item.route}>{item.name}</Link>
                </li>;
            })}
        </ul>;
    };
    return <>{ buildMenu(menuItems) }</>;
};
