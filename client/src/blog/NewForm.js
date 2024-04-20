import React, { useState } from 'react';
import './newform.css';
import { useNavigate } from "react-router-dom"

const NewForm = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [isFormValid, setIsFormValid] = useState(true);
  let navigate = useNavigate();

  const handleTitleChange = (e) => {
    const newTitle = e.target.value;
    setTitle(newTitle);
    checkFormValidity(newTitle, content);
  };

  const handleContentChange = (e) => {
    const newContent = e.target.value;
    setContent(newContent);
    checkFormValidity(title, newContent);
  };

  const checkFormValidity = (newTitle, newContent) => {
    // Check if both title and content are not empty
    setIsFormValid(newTitle.trim() !== '' && newContent.trim() !== '');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!isFormValid) {
      alert("Please fill in both 'Title' and 'Content'");
      return;
    }

    try {
      const response = await fetch('/newarticle', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: title, body: content }),
      });
      if (!response.ok) {
        throw new Error('HTTP error! Status: ${response.status}');
      }
      alert("Article Successfully Posted");

      setTitle('');
      setContent('');
      
      navigate('/blog');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return(
    <div>
      <form onSubmit={handleSubmit}>
      <div className='button-container'>
        <button type="submit"> PUBLISH </button>
      </div>
        <div className='style'>
        <label class="block text-sm font-medium text-green-600">
          Title 
          <input type="text" value={title} onChange={e => setTitle(e.target.value)} required />
        </label>
        <label>
          Body
          <textarea value={content} onChange={e => setContent(e.target.value)} required/>
        </label>
        </div>
      </form>
    </div>
  );
};
export default NewForm;