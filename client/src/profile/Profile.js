import { useState } from 'react'

function Profile(props) {
    const [ profileData, setProfileData ] = useState(null)

    function getData(){
        fetch("/profile", {
            method: "GET",
            headers: {
                Authorization: 'Bearer' + props.token        
            }
        }).then((response) => {
            const res = response.data
            res.access_token && props.setToken(res.access_token)
            setProfileData(({
                profile_name: res.name,
            }))
        }).catch((error) => {
            if(error.response) {
                console.log(error.response)
                console.log(error.response.status)
                console.log(error.response.headers)
            }
        })
    }
    return (
        <div className='profile'>
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        }
        </div>
    );
}

export default Profile