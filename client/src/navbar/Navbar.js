import React from "react";
import { Link } from "react-router-dom";

function NavBar(){
    function logMeOut() {
        
    }
    return(
        <div className='h-[4rem] bg-black text-white flex w-full items-center justify-between'>
            <div className='flex justify-center p-10'>
                 <p className='cursor-pointer font-medium hover:text-green-300'><Link to="/">ExploreKE</Link></p>
            </div>
    
            <div className='hidden w-full lg:flex max-w-[1250px] items-center justify-center space-x-4'>
                <ul className='w-full lg:flex items-center justify-center space-x-4'>
                    <li className='cursor-pointer font-medium hover:text-green-300'><Link to="/">HOME</Link></li>
                    <li className='cursor-pointer font-medium hover:text-green-300'><Link to="/blog">BLOGS</Link></li>
                    <li className='cursor-pointer font-medium hover:text-green-300'><Link to="/about">ABOUT US</Link></li>
                </ul>
            </div>
    
            <div className='flex items-center p-10'>
            <p className='cursor-pointer font-medium hover:text-green-300'><Link to="/login">LogIn</Link></p>
            </div>
        </div>
        )
}

export default NavBar;
