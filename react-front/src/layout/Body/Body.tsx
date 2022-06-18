import {BodyProps} from "./Body.props";
import styles from './Body.module.css';
import cn from "classnames";
import {Badge} from "../../components";


export const Body = ({children, ...props}: BodyProps): JSX.Element => {
    return <div className={cn(styles.body, {})} {...props}>{children}
        <Badge>Hello!</Badge>
    </div>;
};
