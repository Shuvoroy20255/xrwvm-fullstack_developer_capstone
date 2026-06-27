import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const DealerDetail = ({ user }) => {
  const { id } = useParams();
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch(`/api/get_dealer_by_id/?id=${id}`)
      .then(res => res.json())
      .then(data => setDealer(data));
    fetch(`/api/get_dealer_reviews/?dealer_id=${id}`)
      .then(res => res.json())
      .then(data => setReviews(data));
  }, [id]);

  return (
    <div className="container mt-4">
      {dealer && (
        <div>
          <h2>{dealer.full_name}</h2>
          <p>{dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}</p>
        </div>
      )}
      <h3>Reviews</h3>
      {reviews.length === 0 ? <p>No reviews yet.</p> : reviews.map(r => (
        <div key={r.id} className="card mb-2">
          <div className="card-body">
            <p><strong>{r.user_name}</strong> ({r.sentiment})</p>
            <p>{r.review_text}</p>
          </div>
        </div>
      ))}
      {user && <a href={`/post_review/${id}`} className="btn btn-success">Write a Review</a>}
    </div>
  );
};

export default DealerDetail;