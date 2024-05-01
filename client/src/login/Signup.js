import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { TextField, Button, Snackbar } from '@mui/material';

function SignupForm() {
  const { handleSubmit, control } = useForm();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });
  const [successSnackBar, setSuccessSnackBar] = useState(false);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const onSubmit = (data) => {
    try {
      fetch('/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      }).then(() => {
        setSuccessSnackBar(true);
        setTimeout(() => {
            history.pushState('/login')
        }, 2000);
      });
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <div>
      <h1>SignUp</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
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
        message="Signup successful!"
      />
    </div>
  );
}

export default SignupForm;
