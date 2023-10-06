// import logo from './logo.svg';
import './App.css';
import Homepage from './Homepage';
import Pics from './Pics';
import Description from './Description';
import Sketch from './Sketch';
import Catergory from './Catergory';
import {Routes,Route,Link} from 'react-router-dom'
import React from 'react'
import LoginPage from './Login';

function App() {
  return (
    <>
    <div>
      <Link to={'/home'}>Homepage</Link>
      <Link to={'/Pics'}>Pics</Link>
       <Link to={'/Description'}>Description</Link>
      <Link to={'/Sketch'}>Sketch</Link>
      <Link to={'/Category'}>Catergory</Link>
      <Link to={'/Login'}>LoginPage</Link>
    </div>
    <Routes>
      <Route path='/home'element={<Homepage/>}/>
      <Route path='/pics'element={<Pics/>}/>
      <Route path='/description'element={<Description/>}/>
      <Route path='/sketch'element={<Sketch/>}/>
      <Route path='/category'element={<Catergory/>}/>
      <Route path='/login'element={<LoginPage/>}/>
    </Routes>
    {/* <Homepage/>
    <Pics/>
    <Description/>
    <Sketch/>
  <Catergory/> */}
    </>
  );
}

export default App;
