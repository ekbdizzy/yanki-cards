import {Body, Feedback, withLayout} from "../../layout";
import React from "react";

function InterviewPage(): JSX.Element {
    return<>
                <Body>
                    <Feedback/>
                </Body>
    </>;
}

export default withLayout(InterviewPage);

