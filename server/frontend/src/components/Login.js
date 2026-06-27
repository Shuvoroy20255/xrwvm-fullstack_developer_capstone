import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);
    const res = await fetch('/api/login/', {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: formData,
    });
    const data = await res.json();
    if (data.status === 'success') {
      onLogin(data.username);
      navigate('/');
    } else {
      alert('Login failed');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input className="form-control mb-2" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
        <input className="form-control mb-2" type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        <button className="btn btn-primary" type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;