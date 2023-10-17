import React, { useState, useEffect } from 'react';

function Sketch() {
  const [pics, setPics] = useState([]);

  useEffect(() => {
    // Fetch data from the server when the component mounts
    fetch('http://127.0.0.1:5000/pics')
      .then((response) => response.json())
      .then((data) => setPics(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <>
      <h2>Sketch</h2>
      {pics.map((pic, index) => (
        <img key={index} src={pic.image_url} alt={`Sketch ${index + 1}`} />
      ))}

      <form id="comment-form"></form>
      <textarea id="comment-input" placeholder="Write your comments"></textarea>
      <button type="submit">Submit Comment</button>
    </>
  );
}

export default Sketch;
