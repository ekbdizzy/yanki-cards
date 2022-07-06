import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './InterviewPage.module.css';
import { withLayout } from '../../layout';
import { Badge, Button, Htag, Question } from '../../components';
import Duck from '../../assets/images/duck.png';
import { URLS } from '../../api';

const InterviewPage = () => {
  return (
    <>
      <div className="flex h-full">
        <Question/>
        <section className="basis-1/2 p-10">
          <img src={Duck} className='max-h-96 mx-auto' alt="Duck"/>
        </section>
      </div>
    </>
  );
};

export default withLayout(InterviewPage);
