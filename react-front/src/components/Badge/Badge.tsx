import {BadgeProps} from "./Badge.props";
import styles from './Badge.module.css';

export const Badge = ({children, ...props}: BadgeProps): JSX.Element => {
    return <span className={styles.badge}
                 {...props}>{children}</span>;
};
