import { withLayout } from '../../layout';
import { H } from '../../components';
import React from 'react';

const Page404 = () => {
  return <>
    <H tag="h1">Page does not exists</H>
  </>;
};

export default withLayout(Page404);
