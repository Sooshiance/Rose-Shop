import { useState } from 'react'
import { BrowserRouter as Routers, Routes, Route } from 'react-router-dom'
import Login from './pages/auth/Login'
import Home from './pages/home/Home'
import Register from './pages/auth/Register'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Routers>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path='/register' element={<Register />} />
      </Routes>
    </Routers>
  )
}

export default App
