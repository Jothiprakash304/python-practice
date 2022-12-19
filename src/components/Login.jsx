import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import { Link } from "react-router-dom";
import logo from './logo/cloud.jpg'
import C_home from "./cloudpay_home";
import Logindata from "../API_connection/Login";


function Login (){
    const onFinish= async(values)=>{
    const login_detail={
        Email:values.email,
        Password:values.password

    };
    const response=await Logindata(login_detail)
};
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
           <Link to="/"> <li className="nav-item"><a className="nav-link" href="#">Home</a></li></Link> 
            <Link to="/register"><li className="nav-item"><a className="nav-link" href="#">Register</a></li> </Link>
        
        </ul>
       </div>  
    </div>
   </nav>


      <h1 className="text-center my-3">Login</h1>
   <div  className="container">
    <div className="row justify-content-center">
        <div className="col-md-5" >
            <form action="cloudpay_home.jsx">
                Email: <input type="text" id="" name="email" className="form-control"/>
                Password: <input type="text" id="" name="password" className="form-control"/>
                <input className="my-3" type="submit" placeholder="login"/>
            </form>
            <div className="row mb-4">
                <div className="col d-flex justify-content-center">
                    <div className="form-check">
                        <input className="form-check-input" type="checkbox" value='' id="" checked/>
                        <label className="form-check-label">Remember me</label>

                    </div>
                    <div className="col-6">
                       <a href="">Forget Password</a>

                    </div>

                </div>


            </div>
            <h4>Not an user ? <Link to="/register"><button> <a href="" className="color">Register</a></button></Link></h4>

        </div>

    </div>

   </div>
    
        </>
    );
}
export default Login;