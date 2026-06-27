import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

const PostReview = ({ user }) => {
  const { dealer_id } = useParams();
  const navigate = useNavigate();
  const [reviewText, setReviewText] = useState('');
  const [purchase, setPurchase] = useState(false);
  const [carMake, setCarMake] = useState('');
  const [carModel, setCarModel] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/api/post_review/', {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        dealer_id,
        review_text: reviewText,
        purchase,
        car_make: carMake,
        car_model: carModel,
      })
    })
    .then(res => res.json())
    .then(data => {
      if (data.status === 'review created') {
        navigate(`/dealer/${dealer_id}`);
      } else {
        alert('Error');
      }
    });
  };

  if (!user) return <p>Please log in to post a review.</p>;

  return (
    <div className="container mt-4">
      <h2>Post Review</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          className="form-control mb-2"
          rows="4"
          placeholder="Your review..."
          value={reviewText}
          onChange={(e) => setReviewText(e.target.value)}
          required
        ></textarea>
        <div className="form-check mb-2">
          <input className="form-check-input" type="checkbox" checked={purchase} onChange={() => setPurchase(!purchase)} />
          <label className="form-check-label">Purchased a car here?</label>
        </div>
        <input
          type="text"
          className="form-control mb-2"
          placeholder="Car make"
          value={carMake}
          onChange={(e) => setCarMake(e.target.value)}
        />
        <input
          type="text"
          className="form-control mb-2"
          placeholder="Car model"
          value={carModel}
          onChange={(e) => setCarModel(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">Submit Review</button>
      </form>
    </div>
  );
};

export default PostReview;