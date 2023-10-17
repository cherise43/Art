import React from "react";
import "./Sketch.css"; // Import the CSS file

function Sketch() {
  return (
    <div className="sketch-container">
      <h2>Sketch</h2>
      <div className="image-container">
        <img
          src="https://cdn.pixabay.com/photo/2014/11/13/06/12/boy-529067_640.jpg"
          alt="Sketch 1"
        />
        <img
          src="https://cdn.pixabay.com/photo/2016/11/29/12/13/fence-1869401_640.jpg"
          alt="Sketch 2"
        />
        <img
          src="https://cdn.pixabay.com/photo/2012/12/27/19/40/chain-link-72864_640.jpg"
          alt="Sketch 3"
        />
        <img
          src="https://cdn.pixabay.com/photo/2017/09/25/11/55/cyberspace-2784907_640.jpg"
          alt="Sketch 4"
        />
        <img
          src="https://cdn.pixabay.com/photo/2016/02/28/12/55/boy-1226964_640.jpg"
          alt="Sketch 5"
        />
        <img
          src="https://cdn.pixabay.com/photo/2016/02/28/12/55/boy-1226964_640.jpg"
          alt="Sketch 6"
        />
      </div>
      <form id="comment-form">
        <textarea
          id="comment-input"
          placeholder="Write your comments"
        ></textarea>
        <button type="submit" id="submit-button">
          Submit Comment
        </button>
      </form>
    </div>
  );
}

export default Sketch;