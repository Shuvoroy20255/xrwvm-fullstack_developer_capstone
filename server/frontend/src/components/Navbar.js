import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = ({ user, onLogout }) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Cars Dealership</Link>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav me-auto">
            <li className="nav-item"><Link className="nav-link" to="/">Home</Link></li>
            <li className="nav-item"><a className="nav-link" href="/about/">About</a></li>
            <li className="nav-item"><a className="nav-link" href="/contact/">Contact</a></li>
          </ul>
          <ul className="navbar-nav">
            {user ? (
              <>
                <li className="nav-item"><span className="nav-link text-light">Welcome, {user}</span></li>
                <li className="nav-item"><button className="btn btn-link nav-link" onClick={onLogout}>Logout</button></li>
              </>
            ) : (
              <>
                <li className="nav-item"><Link className="nav-link" to="/login">Login</Link></li>
                <li className="nav-item"><Link className="nav-link" to="/register">Register</Link></li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;