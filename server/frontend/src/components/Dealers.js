import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Dealers = ({ user }) => {
  const [dealers, setDealers] = useState([]);
  const [stateFilter, setStateFilter] = useState('');

  const fetchDealers = (state = '') => {
    let url = '/api/get_dealers/';
    if (state) url = `/api/get_dealers_by_state/?state=${state}`;
    fetch(url)
      .then(res => res.json())
      .then(data => setDealers(data));
  };

  useEffect(() => {
    fetchDealers();
  }, []);

  const handleStateFilter = () => {
    fetchDealers(stateFilter);
  };

  return (
    <div className="container mt-4">
      <h2>Our Dealerships</h2>
      {user && (
        <div className="mb-3">
          <input
            type="text"
            placeholder="Filter by state (e.g. Kansas)"
            value={stateFilter}
            onChange={(e) => setStateFilter(e.target.value)}
          />
          <button className="btn btn-primary ms-2" onClick={handleStateFilter}>Filter</button>
        </div>
      )}
      <div className="row">
        {dealers.map(dealer => (
          <div className="col-md-4 mb-3" key={dealer.id}>
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{dealer.full_name}</h5>
                <p>{dealer.city}, {dealer.state}</p>
                <Link to={`/dealer/${dealer.id}`} className="btn btn-info">View Details</Link>
                {user && <Link to={`/post_review/${dealer.id}`} className="btn btn-warning ms-2">Review Dealer</Link>}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dealers;