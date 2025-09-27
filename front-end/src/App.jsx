import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Users from "./pages/Users";
import Habits from "./pages/Habits";
import Challenges from "./pages/Challenges";
import Home from "./pages/Home";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/users" element={<Users />} />
        <Route path="/habits" element={<Habits />} />
        <Route path="/challenges" element={<Challenges />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}
