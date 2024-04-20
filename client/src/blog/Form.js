import React from 'react';

function Form({ title, body, setTitle, setContent, updateArticle}) {
  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleContentChange = (e) => {
    setContent(e.target.value);
  };

  return (
    <div className="p-4 border">
      <input
        className="w-full border rounded mb-2 p-2"
        type="text"
        value={title}
        onChange={handleTitleChange}
        placeholder="Title"
      />
      <textarea
        className="w-full border rounded p-2"
        value={body}
        onChange={handleContentChange}
        placeholder="Content"
      />
      <button
        className="bg-blue-500 hover:bg-blue-700 font-bold py-2 px-4 rounded mt-2"
        onClick={updateArticle}
      >
        Save
      </button>
    </div>
  );
}

export default Form;