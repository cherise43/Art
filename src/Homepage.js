import React, { useState, useEffect } from "react";
import "./Homepage.css"; // Import the CSS file

function Homepage() {
  // Define a state variable to store the list of users
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Make a GET request to fetch the users data
    fetch("http://127.0.0.1:5000/users")
      .then((response) => response.json())
      .then((data) => {
        setUsers(data);
      })
      .catch((error) => {
        console.error("Error fetching users:", error);
      });
  }, []);

  return (
    <div className="homepage">
      <h1>Welcome to the Homepage</h1>
      <h2>Users:</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            User ID: {user.id}, Username: {user.user_name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Homepage;