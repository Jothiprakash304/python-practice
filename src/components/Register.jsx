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



       <h1 className="text-center my-3">Registeration</h1>
       <div className="container">
        <div className="row justify-content-center">
            <div className="col-md-5">
                <form action="" className="form-control">
                    First Name:<input type='text' placeholder="firstname" className="form-control"/>
                    Last Name:<input type='text' placeholder="lastname" className="form-control"/>
                    Email:<input type='text' placeholder="email" className="form-control"/>
                    DOB:<input type='Date' placeholder="" className="form-control"/>
                    Password:<input type='text' placeholder="password" className="form-control"/>
                    Confirm password:<input type='text' placeholder="confirm password" className="form-control"/>

                    <input className="my-4" type='submit' id="" placeholder="submit"/>

                </form>

            </div>

        </div>

       </div>
        
        </>
    );
}

export default Register;