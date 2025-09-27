import React, { useEffect, useState } from "react";

export default function Habits() {
  const [habits, setHabits] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [frequency, setFrequency] = useState("daily");

  const API_URL = "https://health-habit-tracker-1.onrender.com/habits";

  const fetchHabits = () => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setHabits(data));
  };

  useEffect(() => {
    fetchHabits();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, frequency, start_date: new Date().toISOString().slice(0, 10) }),
    })
      .then((res) => res.json())
      .then(() => {
        setTitle(""); setDescription(""); setFrequency("daily");
        fetchHabits();
      });
  };

  const handleDelete = (id) => {
    fetch(`${API_URL}/${id}`, { method: "DELETE" })
      .then(() => fetchHabits());
  };

  const handleUpdate = (habit) => {
    const newFreq = habit.frequency === "daily" ? "weekly" : "daily";
    fetch(`${API_URL}/${habit.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ frequency: newFreq }),
    }).then(() => fetchHabits());
  };

  return (
    <div className="container">
      <h2>Habits</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: "1rem" }}>
        <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <input type="text" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
        <select value={frequency} onChange={(e) => setFrequency(e.target.value)}>
          <option value="daily">Daily</option>
          <option value="weekly">Weekly</option>
        </select>
        <button type="submit">Add Habit</button>
      </form>

      <ul>
        {habits.map((habit) => (
          <li key={habit.id}>
            <strong>{habit.title}</strong> ({habit.frequency})<br />
            {habit.description}<br />
            <button onClick={() => handleUpdate(habit)}>Toggle Frequency</button>
            <button onClick={() => handleDelete(habit.id)} style={{ marginLeft: "0.5rem", color: "red" }}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
