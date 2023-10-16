import React from 'react';

function Sketch() {
  return (
    <>
      <h2>Sketch</h2>
      <img src="https://images.app.goo.gl/NuNHS1ACxDHerVaa8" alt="Sketch 1" />
      <img src="https://images.app.goo.gl/vsXGxjcJbZPYEgUe7" alt="Sketch 2" />
      <img src="https://images.app.goo.gl/HzKp9e55ZJCYartf8" alt="Sketch 3" />
      <img src="https://images.app.goo.gl/Tyg3cyQVv8X8NKsk7" alt="Sketch 4" />
      <img src="https://images.app.goo.gl/ad8QRbSiaV2ogjfo7" alt="Sketch 5" />
      <img src="https://images.app.goo.gl/Xy8wJMPefAXEteJ77" alt="Sketch 6" />

      <form id="comment-form"></form>
      <textarea id="comment-input" placeholder="Write your comments"></textarea>
      <button type="submit">Submit Comment</button>
    </>
  );
}

export default Sketch;
