import React, { useState } from "react";
import { submitText } from "../api";

function InputForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await submitText(text);
    setResult(response);
  };

  return (
    <div>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleSubmit}>Generate</button>
      {result && (
        <div>
          <p>ID: {result.id}</p>
          <p>Link: {result.link}</p>
          <p>Text: {result.text}</p>
          <p>Status: {result.status}</p>
        </div>
      )}
    </div>
  );
}

export default InputForm;
