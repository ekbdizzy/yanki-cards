import {BodyProps} from "./Body.props";
import styles from './Body.module.css';
import cn from "classnames";
import {Badge, Helper} from "../../components";


export const Body = ({children, ...props}: BodyProps): JSX.Element => {
    return <div className={cn(styles.body, {})} {...props}>{children}
        <div className={styles.badges}>
            <Badge>Hello!</Badge>
            <Helper size='small' icon='add'>New question</Helper>
            <Helper size='medium' icon='update'>New question</Helper>
            <Helper size='medium' icon='save'>Add new word</Helper>
            <Helper size='small' icon='export'>Export to CSV</Helper>
        </div>
    </div>;
};
