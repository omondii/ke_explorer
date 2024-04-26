import { useState } from 'react';

/**
 * useToken: handles token operation in the frontend
 * @returns 
 */

function useToken() {
    /**
     * getToken: retrieves the token stored in the localStorage
     * @returns token(if it exists)
     */
    function getToken() {
        const userToken = localStorage.getItem('token');
        return useToken && userToken
    }

    const [ token, setToken ] = useState(getToken());
    /**
     * saveToken: handles storage of token obtained after user login
     * @param {*} userToken 
     */
    function saveToken(userToken) {
        localStorage.setItem('token', userToken);
        setToken(userToken)
    };

    /**
     *removeToken: deletes the token from localStorage and sets the token back to null 
     */
    function removeToken(){
        localStorage.setItem('token');
        setToken(null);
    }

    return {
        setToken: saveToken,
        token,
        removeToken
    }
}

export default useToken;