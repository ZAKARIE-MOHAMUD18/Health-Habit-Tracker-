// src/pages/Home.jsx
import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";

export default function Home() {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Health Habit Tracker</h1>
        <p>Welcome! Stay on top of your habits and challenges.</p>
      </header>

      <main className="home-main">
        <div className="home-card">
          <h2>Users</h2>
          <p>See all users who are tracking their health habits.</p>
          <Link to="/users" className="home-btn">Go to Users</Link>
        </div>

        <div className="home-card">
          <h2>Habits</h2>
          <p>Create, view, and manage your daily or weekly habits.</p>
          <Link to="/habits" className="home-btn">Go to Habits</Link>
        </div>

        <div className="home-card">
          <h2>Challenges</h2>
          <p>Join challenges and track your progress over time.</p>
          <Link to="/challenges" className="home-btn">Go to Challenges</Link>
        </div>
      </main>
    </div>
  );
}
