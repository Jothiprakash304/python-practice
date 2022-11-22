import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import logo from './logo/cloud.jpg'


function Login (){
    return(
        <>
         <nav className="navbar navbar-inverse navbar-fixed-top bg-light">
    <div className="container-fluid">
      <h3> <img src={logo} alt="photo" width={'50px'}/> Cloud pay</h3>
       {/* <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
        <span className="navbar-toggler-icon"></span>
       </button> */}
       <div className="navbar- justify-content-end" id="navbar">
        <ul className="nav">
            <li className="nav-item"><a className="nav-link" href="#">Home</a></li> 
            <li className="nav-item"><a className="nav-link" href="#">Register</a></li> 
        
        </ul>
       </div>  
    </div>
   </nav>


      <h1 className="text-center my-3">Login</h1>
   <div  className="container">
    <div className="row justify-content-center">
        <div className="col-md-5" >
            <form action="">
                Username: <input type="text" id="" name="" className="form-control"/>
                Password: <input type="text" id="" name="" className="form-control"/>
                <input className="m-sm-4" type="submit" placeholder="login"/>
            </form>

        </div>

    </div>

   </div>
    
        </>
    );
}
export default Login;