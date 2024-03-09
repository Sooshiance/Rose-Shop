import axios from 'axios'
import { isAccessTokenExpired, setAuthUser, getRefreshToken } from './auth'
import baseURL from './constants'
import Cookies from 'js-cookie'


const useAxios = async () => {
    const access_token = Cookies.get("access_token")
    const refresh_token = Cookies.get("refresh_token")

    const axiosInstance = axios.create({
        baseURL: baseURL,
        headers: { Authorization: `Bearer ${access_token}` }
    })

    axiosInstance.interceptors.request.use(async (req) => {
        if (!isAccessTokenExpired) {
            return req;
        }
        const response = await getRefreshToken(refresh_token)

        setAuthUser(response.access, response.refresh)

        req.headers.Authorization = `Bearer ${response.data.access}`

        return req;
    })

    return axiosInstance;
}

export default useAxios