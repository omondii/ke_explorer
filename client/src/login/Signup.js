import { useState } from "react";
import { useForm, Controller } from 'react-hook-form';
import { TextField, Button, Snackbar } from '@mui/material';


function SigupForm(){ 
    const { handleSubmit, control } = useForm();
    const { successSnackBar, setSuccessSnackBar } = useState(false);

    const onSubmit = (data) => {
        try{
            fetch('/signup', {
                method: "POST",
                headers: {
                    "content-type": "application/json",
                },
                body: JSON.stringify(data)
            }).then(setSuccessSnackBar(true));
            setTimeout(() => {
                history.pushState('/login');
            }, 2000);
        } catch(error) {
            console.log('Error submitting form:', error)
        }
    };
    return (
        <div>
            <h1>SignUp</h1>
            <form onSubmit={handleSubmit}>
            <div>
                <TextField
                id="username"
                name="username"
                label="Username"
                value={formData.username}
                onChange={handleInputChange}
                />
            </div>
            <div>
                <TextField
                id="email"
                name="email"
                label="Email"
                type="email"
                value={formData.email}
                onChange={handleInputChange}
                />
            </div>
            <div>
                <TextField
                id="password"
                name="password"
                label="Password"
                type="password"
                value={formData.password}
                onChange={handleInputChange}
                />
            </div>
            <Button variant="contained" color="primary" type="submit">
                Submit
            </Button>
            </form>
            <Snackbar 
            open={successSnackBar}
            autoHideDuration={3000}
            onClose={() => setSuccessSnackBar(false)}
            message="Sigup Successful!"
            />
        </div>
    );
}

export default SigupForm;