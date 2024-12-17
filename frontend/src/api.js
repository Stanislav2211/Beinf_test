export async function submitText(text) {
    const response = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    return await response.json();
  }
  