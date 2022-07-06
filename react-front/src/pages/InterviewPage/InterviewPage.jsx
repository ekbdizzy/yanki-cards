import React, { useEffect, useState } from 'react';
import styles from './InterviewPage.module.css';
import { withLayout } from '../../layout';
import { Badge, Button, Htag } from '../../components';

const InterviewPage = () => {
  return (
    <>
      <div className={styles.main}>
        <section>
          <div className="flex items-center">
            <Badge>Career</Badge>
            <Button icon="refresh" >New question</Button>
          </div>
          <Htag>Tell me about yourself and what do you think about global warmness?</Htag>
          <Button color='fuchsia' icon="refresh">What do you think about global warmness?</Button>
        </section>
      </div>
    </>
  );
};

export default withLayout(InterviewPage);
