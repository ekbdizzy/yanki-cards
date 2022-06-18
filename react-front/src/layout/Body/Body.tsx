import {BodyProps} from "./Body.props";
import styles from './Body.module.css';
import cn from "classnames";
import {Badge, Header, Helper, Input, Listener, P} from "../../components";


export const Body = ({children, ...props}: BodyProps): JSX.Element => {
    return <div className={cn(styles.body, {})} {...props}>{children}
        <Listener person='duck'/>
        <Header tag={'h1'}>What is the capital of great britain?</Header>
        <Header tag={'h2'}>Tell me about yourself and what do you think about global warmness?</Header>
        <div className={styles.badges}>
            <Badge>Hello!</Badge>
            <Helper size='small' icon='add'>New question</Helper>
            <Helper size='medium' icon='update'>New question</Helper>
            <Helper size='medium' icon='save'>Add new word</Helper>
            <Helper size='small' icon='export'>Export to CSV</Helper>
        </div>
        <div>
            <P color='purple' size='big'>Apple</P>
            <P color='cyan' size='normal'>Have you ever heard about something new, than can be cause of new global warmness?</P>
            <P>What do you think about global warmness?</P>
        </div>
        <div>
            <Input value={'Need new word?'} />
        </div>
    </div>;
};
