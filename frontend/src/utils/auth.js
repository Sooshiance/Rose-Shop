import { useAuthStore } from '../store/auth'
import APICall from './proxyURL'
import jwt_decode from 'jwt-decode'
import Cookies from 'js-cookie'
import axios from 'axios'


export const login = async (phone, password) => {
    try {
        const { data, status } = await APICall.post("user/token/", { phone, password })

        if (status === 200) {
            setAuthUser(data.access, data.refresh)
        }
        return { data, error: null }
    } catch (error) {
        console.log(error)
        return {
            data: null,
            error: error.response.data?.detail || "something went wrong!"
        };
    }
}


export const register = async (phone, password, password2, email, username, full_name) => {
    try {
        const { data } = await axios.post("user/register/", {
            phone, password, password2, email, username, full_name
        })

        await login(phone, password)

        return { data, error: null }

    } catch (error) {
        console.log(error)
        return {
            data: null,
            error: error.response.data?.detail || "something went wrong!"
        }
    }
}

export const logout = () => {
    Cookies.remove("access_token")
    Cookies.remove("refresh_token")
    useAuthStore.getState().setUser(null)
}

export const setUser = async () => {
    const accessToken = Cookies.get("access_token")
    const refreshToken = Cookies.get("refresh_token")

    if (!accessToken || !refreshToken) {
        return;
    }

    if (isAccessTokenExpired(accessToken)) {
        const response = await getRefreshToken(refreshToken)

        setAuthUser(response.access, response.refresh)
    } else {
        setAuthUser(accessToken, refreshToken)
    }
}

export const setAuthUser = (access_token, refresh_token) => {
    Cookies.set("access_token", access_token, {
        expires: 1,
        secure: true
    })

    Cookies.set("refresh_token", refresh_token, {
        expires: 7,
        secure: true
    })

    const user = jwt_decode(access_token) ?? null

    if (user) {
        useAuthStore.getState().setUser(user)
    }
    useAuthStore.getState().Loading(false)
}

export const getRefreshToken = async () => {
    const refresh_token = Cookies.get("refresh_token")

    const response = await APICall.post("user/token/refresh/", {
        refersh: refresh_token
    })

    return response.data
}

export const isAccessTokenExpired = (accessToken) => {
    try {
        const decodeToken = jwt_decode(accessToken)

        return decodeToken.exp < Date.now() / 100
    } catch (error) {
        console.log(error)
        return true;
    }
}