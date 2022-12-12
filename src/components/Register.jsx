import React,{Component} from "react";
import logo from './logo/cloud.jpg'
import { useState } from "react";
import { Link } from "react-router-dom";
import Registerdata from "../API_connection/Register";


function Register(){
    const onFinish =async(values)=>{
        const userdata ={
            First_name:values.f_name,
            Last_name:values.l_name,
            Email:values.email,
            Dob:values.birth,
            Password:values.password,
            Confirm_password:values.c_password,
        };
        const response =await Registerdata(userdata);    
    };
    // const onFinishFailed = (errorinfo) =>{

    // }
    return(
        <>    <nav className="navbar navbar-inverse navbar-fixed-top bg-light">
        <div className="container-fluid">
          <h3> <img src={logo} alt="photo" width={'50px'}/> Cloud pay</h3>
           {/* <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
            <span className="navbar-toggler-icon"></span>
           </button> */}
           <div className="navbar- justify-content-end" id="navbar">
            <ul className="nav">
               <Link to="/"><li className="nav-item"><a className="nav-link" href="#">Home</a></li> </Link> 
               <Link to="/login"> <li className="nav-item"><a className="nav-link" href="#">Login</a></li> </Link>
            
            </ul>
           </div>  
        </div>
       </nav>



       <h1 className="text-center my-3">Registeration</h1>
       
       <div className="container">
        <div className="row justify-content-center">
            <div className="col-md-5">
                <form action=""className="form-control">
                    First Name:<input type='text' name="f_name" placeholder="firstname" className="form-control" required/>
                    Last Name:<input type='text'name="l_name" placeholder="lastname" className="form-control" required/>
                    Email:<input type='text'name="email" placeholder="email" className="form-control" required/>
                    DOB:<input type='Date' name="birth" placeholder="" className="form-control" required/>
                    Password:<input type='text'name="password" placeholder="password" className="form-control" required/>
                    Confirm password:<input type='text' name="c_password" placeholder="confirm password" className="form-control"required/>

                    <input className="my-4" type='submit' id="" onClick={onFinish} placeholder="submit"/>
                    

                </form>

            </div>

        </div>

       </div>
        
        </>
    );
}

export default Register;