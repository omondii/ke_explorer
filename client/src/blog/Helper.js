import React, { useState } from 'react';
import NewForm from './NewForm';

function HelperComponent() {
    const[title, setTitle] = useState('');
    const[content, setContent] = useState('');

    const insertArticle = async (article) => {
        const response = await fetch(`/newarticle`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(article),
        });
        if (!response.ok) {
            throw new Error('HTTP error' + response.status);
        }
    };
    return (
        <NewForm
        title={title}
        body={content}
        setTitle={setTitle}
        setContent={setContent}
        insertArticle={insertArticle}
        />
    )
}

export  default HelperComponent;