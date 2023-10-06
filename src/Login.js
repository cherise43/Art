import React, { useState } from "react";
import "./App.css"; 

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("")
  const handleLogin = (e) => {
    e.preventDefault();


    if (email === "user@example.com" && password === "password") {
      alert("Login successful!");
    } else {
      alert("Login failed. Please check your credentials.");
    }
  };

  return (
    <div id="login-container">
      <h1>Login</h1>
      <form id="login-form" onSubmit={handleLogin}>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" id="login-button">Login</button>
      </form>
    </div>
  );
}

export default LoginPage;
