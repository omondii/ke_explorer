import React, { useState, useEffect } from 'react';
import { FaEdit, FaTrash } from 'react-icons/fa';
import { useNavigate, Link } from 'react-router-dom';
import Form from './Form';
import NewForm from './NewForm';
import './blog.css'

function Blog({ articles, editArticle, setArticles }) {
  const [isAddingNewArticle, setIsAddingNewArticle] = useState(false);
  const [editedArticle, setEditedArticle] = useState(null);

  const [editedTitle, setEditedTitle] = useState('');
  const [editedContent, setEditedContent] = useState('');
  const  navigate = useNavigate();
  // const navigate = useNavigate();

  // const handleViewArticle = (articleId) => {
  //   // Redirect to a new page to view the full article
  //   navigate(`/article/${articleId}`);
  // };

  useEffect(() => {
    fetch(`/articles`)
      .then((response) => response.json())
      .then((data) => setArticles(data))
      .catch((error) => console.error('Error fetching articles:', error));
  }, [setArticles]);

  const handleEditArticle = (article) => {
    setEditedArticle(article);
    setEditedTitle(article.title);
    setEditedContent(article.body);
  };

  const addNewArticle = () => {
    navigate('/new-article');
    setIsAddingNewArticle(true);
    setEditedArticle(null);
    setEditedTitle('');
    setEditedContent('');
  };

  const insertArticle = (newArticle) => {
    fetch(`/newarticle`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: newArticle.title,
        body: newArticle.content,
      }),
    })
      .then((response) => {
        if (response.ok) {
          fetch(`/articles`)
            .then((response) => response.json())
            .then((data) => setArticles(data))
            .catch((error) =>
              console.error('Error fetching articles after insert:', error)
            );
        } else {
          throw new Error('Insert failed');
        }
      })
      .catch((error) => {
        console.error('Error inserting article:', error);
      });
  };

  const deleteArticle = (articleId) => {
    fetch(`/article/${articleId}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.ok) {
          fetch('/get')
            .then((response) => response.json())
            .then((data) => setArticles(data))
            .catch((error) =>
              console.error('Error fetching articles after delete:', error)
            );
        } else {
          throw new Error('Delete failed');
        }
      })
      .catch((error) => {
        console.error('Error deleting article:', error);
      });
  };

  const updateArticle = () => {
    if (editedArticle) {
      const updatedArticle = {
        id: editedArticle.id,
        title: editedTitle,
        body: editedContent,
      };

      fetch(`/articleupdate/${editedArticle.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedArticle),
      })
        .then((response) => {
          if (response.ok) {
            setEditedArticle(null);
            setEditedTitle('');
            setEditedContent('');
            fetch('/articles')
              .then((response) => response.json())
              .then((data) => setArticles(data))
              .catch((error) =>
                console.error('Error fetching articles after update:', error)
              );
          } else {
            throw new Error('Update failed');
          }
        })
        .catch((error) => {
          console.error('Error updating article:', error);
        });
    }
  };

  return (
    <div className="mainpost" style={{}} >
      <div style={{justifyContent: 'center', alignItems: 'right', display: 'flex' }}>
      <button
        className="newbtn"
        onClick={addNewArticle}
      >
        New Post
      </button>
      </div >
      
      <div className="">
        <div className="post">
        {articles.map((article) => (
          <div key={article.id} style = {{paddingBottom: 15}}>
            <div style={{display: 'flex', fontStyle: 'italic', paddingBottom: '5px', color: 'green'}}>
              <p>By:Joe Doe</p>
            
              <p style={{paddingLeft: '10px'}}>{article.new_date}</p>
              </div>
              <h2 style={{fontSize:'20px', fontWeight: 'bold' }}>
              <Link to={`/article/${article.id}`}>{article.title} </Link>
              </h2>
            <p className="paragraph">
              <Link to={`/article/${article.id}`}>{article.body}</Link>
              </p>
            {/* <div>
                <button
                  className="viewbtn"
                  onClick={() => handleViewArticle(article.id)}
                >
                  
                </button>
              </div> */}

            <div style={{paddingBottom: 15, justifyContent: 'right', alignContent: 'right'}}>
              <button
                className="editbtn"
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
            </div>
            <hr/>
          </div>
        ))}
        

        {editedArticle && (
          <Form
            title={editedTitle}
            body={editedContent}
            setTitle={setEditedTitle}
            setContent={setEditedContent}
            updateArticle={updateArticle}
          />
        )}

        {isAddingNewArticle && (
          <NewForm
            title={editedTitle}
            body={editedContent}
            setTitle={setEditedTitle}
            setContent={setEditedContent}
            insertArticle={insertArticle}
          />
        )}
        </div>
        
      </div>
    </div>
    
  );
}

export default Blog;
