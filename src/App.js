import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Homepage from './Homepage';
import Pics from './Pics';
import Description from './Description';
import Sketch from './Sketch';
import Category from './Category';
import LoginPage from './Login';

function App() {
  return (
    <>
      {/* Navigation Links */}
      <div>
        <Link to="/login">LoginPage</Link>
        <Link to="/home">Homepage</Link>
        <Link to="/pics">Pics</Link>
        <Link to="/description">Description</Link>
        <Link to="/sketch">Sketch</Link>
        <Link to="/category">Category</Link>
      </div>

      {/* Routing */}
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/home" element={<Homepage />} />
        <Route path="/pics" element={<Pics />} />
        <Route path="/description" element={<Description />} />
        <Route path="/sketch" element={<Sketch />} />
        <Route path="/category" element={<Category />} />
      </Routes>
    </>
  );
}

export default App;
