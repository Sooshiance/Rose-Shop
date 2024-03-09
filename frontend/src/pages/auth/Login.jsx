import React, { useState, useEffect } from 'react'
import { login } from '../../utils/auth'
import { useNavigate, Link } from 'react-router-dom'
import { useAuthStore } from '../../store/auth'

function Login() {
    const [phone, setPhone] = useState("")
    const [password, setPassword] = useState("")
    const [isLoading, setIsLoading] = useState(false)

    const navigate = useNavigate()

    const isLoggedIn = useAuthStore((state) => state.isLoggedIn)

    useEffect(() => {
        if (isLoggedIn()) {
            navigate('/')
        }
    })

    const resetForm = () => {
        setPhone("")
        setPassword("")
    }

    const loginHandler = (e) => {
        e.preventDefault()
        setIsLoading(true)

        const { error } = login(phone, password)

        if (error) {
            alert(error)
        } else {
            navigate('/')
            resetForm()
        }

        setIsLoading(false)
    }

    return (
        <div>
            Login page
            <form onSubmit={loginHandler}>
                <label>
                    Phone
                </label>
                <input type="number" name="phone" value={phone} onChange={(e) => setPhone(e.target.value)} />
                <br />
                <br />
                <label>
                    Password
                </label>
                <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <br />
                <br />
                <button type="submit">
                    Login
                </button>
            </form>
        </div>
    )
}

export default Login
