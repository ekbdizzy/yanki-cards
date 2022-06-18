import {BodyProps} from "./Body.props";
import styles from './Body.module.css';
import cn from "classnames";
import {Badge, Header, Helper} from "../../components";


export const Body = ({children, ...props}: BodyProps): JSX.Element => {
    return <div className={cn(styles.body, {})} {...props}>{children}
        <Header tag={'h1'}>What is the capital of great britain?</Header>
        <Header tag={'h2'}>Tell me about yourself and what do you think about global warmness?</Header>
        <div className={styles.badges}>
            <Badge>Hello!</Badge>
            <Helper size='small' icon='add'>New question</Helper>
            <Helper size='medium' icon='update'>New question</Helper>
            <Helper size='medium' icon='save'>Add new word</Helper>
            <Helper size='small' icon='export'>Export to CSV</Helper>
        </div>
    </div>;
};
