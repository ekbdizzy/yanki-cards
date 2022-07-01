import {withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function Page404(): JSX.Element {
    return <>
        <H tag='h1'>Page does not exists</H>
    </>;
}

export default withLayout(Page404);

