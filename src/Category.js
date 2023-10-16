import React, { useState, useEffect } from "react";
import "./Category.css"; // Import the CSS file

function Category() {
  // Define a state variable to store the list of artists
  const [artists, setArtists] = useState([]);

  useEffect(() => {
    // Make a GET request to fetch the artists data
    fetch("http://127.0.0.1:5000/artists")
      .then((response) => response.json())
      .then((data) => {
        setArtists(data);
      })
      .catch((error) => {
        console.error("Error fetching artists:", error);
      });
  }, []);

  return (
    <div id="category-container">
      <h1>Category</h1>
      <p>Artists can send their artist statement for professional review</p>

      <h2>Artists:</h2>
      <ul>
        {artists.map((artist) => (
          <li key={artist.id}>
            Name: {artist.name}, Rating: {artist.rating}, Price: {artist.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Category;