import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h1>Health Tracker</h1>
      <div className="links">
        <Link to="/users">Users</Link>
        <Link to="/habits">Habits</Link>
        <Link to="/challenges">Challenges</Link>
        <Link to="/">Home</Link>
      </div>
    </nav>
  );
}
