import {Body, Feedback, withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function MainPage(): JSX.Element {
    return <>
        <H tag='h1'>Main Page</H>
    </>;
}

export default withLayout(MainPage);

