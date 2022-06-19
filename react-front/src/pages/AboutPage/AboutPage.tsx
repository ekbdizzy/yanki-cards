import {withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function AboutPage(): JSX.Element {
    return <>
        <H tag='h1'>About Page</H>
    </>;
}

export default withLayout(AboutPage);

