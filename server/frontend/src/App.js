import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dealers from './components/Dealers';
import DealerDetail from './components/DealerDetail';
import PostReview from './components/PostReview';
import Login from './components/Login';
import Register from './components/Register/Register';
import Navbar from './components/Navbar';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch('/api/check_auth/', { credentials: 'include' })
      .then(res => res.json())
      .then(data => {
        if (data.username) setUser(data.username);
      })
      .catch(() => {});
  }, []);

  const handleLogin = (username) => setUser(username);
  const handleLogout = async () => {
    await fetch('/api/logout/', { method: 'POST', credentials: 'include' });
    setUser(null);
  };

  return (
    <Router>
      <Navbar user={user} onLogout={handleLogout} />
      <Routes>
        <Route path="/" element={<Dealers user={user} />} />
        <Route path="/dealer/:id" element={<DealerDetail user={user} />} />
        <Route path="/post_review/:dealer_id" element={<PostReview user={user} />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;