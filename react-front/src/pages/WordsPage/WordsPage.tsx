import {withLayout} from "../../layout";
import {H} from '../../components';
import React from "react";

function WordsPage(): JSX.Element {
    return <>
        <H tag='h1'>Words</H>
    </>;
}

export default withLayout(WordsPage);

