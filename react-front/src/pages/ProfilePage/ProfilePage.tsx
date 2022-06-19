import {withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function ProfilePage(): JSX.Element {
    return <>
        <H tag='h1'>Profile</H>
    </>;
}

export default withLayout(ProfilePage);
