import {withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function LogoutPage(): JSX.Element {
    return <>
        <H tag='h1'>Logout Page</H>
    </>;
}

export default withLayout(LogoutPage);

