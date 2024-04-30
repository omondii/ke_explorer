import React, { useState, useEffect } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Switch from 'react-router-dom';
import Home from './home/Home';
import About from './about/About';
import NavBar from './navbar/Navbar';
import Blog from './blog/Blog';
import Contact from './contact/Contact';
import FullArticle from './blog/FullArticle';
import NewForm from './blog/NewForm';
import useToken from './login/useToken';
import Login from './login/Login';
import Profile from './profile/Profile';
import Signup from  './login/Signup';


function App() {
  const [articles, setArticles] = useState([]);
  const { token, removeToken, setToken} = useToken();

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setArticles(resp))
      .catch((err) => console.log(err));
  }, []);

  return (
    <BrowserRouter>
      <div>
        <NavBar/>
      </div>

      <Routes>
        <Switch>
          <Route path="/sigup" exact Component={Signup} />
          {!token ? (
            <Route path="/login" element={<Login setToken={setToken} />} />
          ) : (
            <>
            <Route path="/profile" element={<Profile token={token} setToken={setToken}/>}/>
            </>
          )}
        </Switch>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/blog"
          element={<Blog articles={articles} setArticles={setArticles} />}
        />
        <Route path="/contact" element={<Contact />} />
        <Route path="/article/:articleId" element={<FullArticle/>} />
        <Route path="/new-article" element={<NewForm />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;