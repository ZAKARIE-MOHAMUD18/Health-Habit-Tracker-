import React, { useEffect, useState } from "react";

export default function Challenges() {
  const [challenges, setChallenges] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const API_URL = "https://health-habit-tracker-1.onrender.com/challenges";

  const fetchChallenges = () => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setChallenges(data));
  };

  useEffect(() => {
    fetchChallenges();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, start_date: new Date().toISOString().slice(0,10), end_date: new Date().toISOString().slice(0,10) }),
    }).then(() => {
      setTitle(""); setDescription("");
      fetchChallenges();
    });
  };

  const handleDelete = (id) => {
    fetch(`${API_URL}/${id}`, { method: "DELETE" })
      .then(() => fetchChallenges());
  };

  return (
    <div className="container">
      <h2>Challenges</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
        <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <button type="submit">Add Challenge</button>
      </form>

      <ul>
        {challenges.map((chal) => (
          <li key={chal.id}>
            <strong>{chal.title}</strong><br />
            {chal.description}<br />
            <button onClick={() => handleDelete(chal.id)} style={{ color: "white" }}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
