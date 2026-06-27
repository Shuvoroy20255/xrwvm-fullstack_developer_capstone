import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: form.username,
        first_name: form.firstName,
        last_name: form.lastName,
        email: form.email,
        password: form.password,
      })
    });
    if (res.ok) {
      alert('Registration successful. Please log in.');
      navigate('/login');
    } else {
      alert('Registration failed');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <input className="form-control mb-2" name="username" placeholder="Username" onChange={handleChange} required />
        <input className="form-control mb-2" name="firstName" placeholder="First Name" onChange={handleChange} required />
        <input className="form-control mb-2" name="lastName" placeholder="Last Name" onChange={handleChange} required />
        <input className="form-control mb-2" name="email" type="email" placeholder="Email" onChange={handleChange} required />
        <input className="form-control mb-2" name="password" type="password" placeholder="Password" onChange={handleChange} required />
        <button className="btn btn-primary" type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;