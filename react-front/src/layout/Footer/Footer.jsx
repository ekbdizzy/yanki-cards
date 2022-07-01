import {FooterProps} from "./Footer.props";
import styles from "./Footer.module.css";
import cn from "classnames";


export const Footer = ({children, ...props}: FooterProps): JSX.Element => {
    return <footer className={cn(styles.footer, {})}
                   {...props}>
        Some info in footer
        {children}
        footer
    </footer>;
};
