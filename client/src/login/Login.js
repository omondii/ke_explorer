import { useState } from 'react';


function Login(props) {
    const [loginForm, setLoginForm] = useState({
        email: "",
        password: ""
    })

    function logMeIn(event) {
        fetch('/token', {
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify({
                email: loginForm.email,
                password: loginForm.password,
            }),
        }).then((response) => response.json())
          .then((data) => {
            props.setToken(data.access_token);
        }).catch((error) => {
            console.error("Error fetching token:", error)
        });

        setLoginForm(({
            email: "",
            password: ""
        }))
        event.preventDefault()
    }

    function handleSubmit(event) { 
        const {value, name} = event.target
        setLoginForm(prevNote => ({
            ...prevNote, [name]: value})
        )}
    
    return (
        <div>
            <h1>Login</h1>
            <form className='login'>
                <input 
                onSubmit={handleSubmit}
                    type="email"
                    text={loginForm.email}
                    name="email"
                    placeholder='abc@host.com'
                    value={loginForm.email} />
                <input onSubmit={handleSubmit}
                    type='password'
                    text={loginForm.password}
                    name='password'
                    placeholder='password'
                    value={loginForm.password}/>
                <button onClick={logMeIn}>Submit</button>
            </form>
            <header className="App-header">
                <button onClick={logMeOut}> 
                    Logout
                </button>
           </header>
        </div>
    );
}

export default Login;