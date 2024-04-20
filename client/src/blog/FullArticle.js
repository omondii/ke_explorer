import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './blog.css'

function FullArticle() {
  const { articleId } = useParams(); // Get the articleId from the URL params
  const [article, setArticle] = useState(null);

  useEffect(() => {
    // Fetch the detailed information of the article using the articleId
    fetch(`/article/${articleId}`)
      .then((response) => response.json())
      .then((data) => setArticle(data))
      .catch((error) => console.error('Error fetching article:', error));
  }, [articleId]);

  if (!article) {
    return <div>Loading...</div>; // Display a loading message while fetching data
  }

  return (
    <div className="singlePost">
        <div style={{display: 'flex', fontStyle: 'italic', paddingBottom: '5px', color: 'green'}}>
              <p>By:Joe Doe</p>
            
              <p style={{paddingLeft: '10px'}}>{article.new_date}</p>
              </div>
        <h1 style={{fontSize:'20px', fontWeight: 'bold'}}>{article.title}</h1>
        <p className="singleParagraph">{article.body}</p>
        {/* <div style={{paddingBottom: 15, justifyContent: 'right', alignContent: 'right'}}>
              <button
                class="editbtn"
                onClick={() => handleEditArticle(article)}
              >
                <FaEdit/>
              </button>
              <button
                className="deletebtn"
                onClick={() => deleteArticle(article.id)}
              >
                <FaTrash/>
              </button>
            </div> */}
    
    </div>
  );
}

export default FullArticle;
