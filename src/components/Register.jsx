import React from "react";
import logo from './logo/cloud.jpg'


function Register(){
    return(
        <>    <nav className="navbar navbar-inverse navbar-fixed-top bg-light">
        <div className="container-fluid">
          <h3> <img src={logo} alt="photo" width={'50px'}/> Cloud pay</h3>
           {/* <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
            <span className="navbar-toggler-icon"></span>
           </button> */}
           <div className="navbar- justify-content-end" id="navbar">
            <ul className="nav">
                <li className="nav-item"><a className="nav-link" href="#">Home</a></li> 
                <li className="nav-item"><a className="nav-link" href="#">Login</a></li> 
            
            </ul>
           </div>  
        </div>
       </nav>
        
        </>
    );
}

export default Register;