import React, { useEffect, useState } from 'react';
import styles from './InterviewPage.module.css';
import { withLayout } from '../../layout';

const InterviewPage = () => {
  return (
    <>
      <div className={styles.main}>
        <section>
          InterviewPage
        </section>
      </div>
    </>
  );
};

export default withLayout(InterviewPage);
