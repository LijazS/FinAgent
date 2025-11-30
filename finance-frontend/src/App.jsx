import React,{ useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import axios from 'axios'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import LandingPage from './LandingPage.jsx'
import Signup from './pages/Signup.jsx'
import Signin from './pages/Signin.jsx'
import Dashboard from './pages/Dashboard.jsx'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage/>} />
          <Route path="/signup" element={<Signup/>} />
          <Route path="/signin" element={<Signin/>} />
          <Route path="/dashboard" element={<Dashboard/>} />
        </Routes>
      </Router>
   </>
  )
}

export default App
