import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import { Link } from "react-router-dom";
import logo from './logo/cloud.jpg'
import img1 from './logo/pay1.jpg'
import img2 from './logo/pay2.jpeg'
import img3 from './logo/pay4.jpg'


function BasicExample() {
  return (
    <>
   <nav className="navbar navbar-inverse navbar-fixed-top bg-light">
    <div className="container-fluid">
      <h3> <img src={logo} alt="photo" width={'50px'}/> Cloud pay</h3>
       {/* <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
        <span className="navbar-toggler-icon"></span>
       </button> */}
       <div className="navbar- justify-content-end" id="navbar">
        <ul className="nav">
           <Link to="/login" > <li className="nav-item"><a className="nav-link" href="#">Login</a></li> </Link>
           <Link to="/register"> <li className="nav-item"><a className="nav-link" href="#">Register</a></li> </Link>
        </ul>
       </div>  
    </div>
   </nav>

   

   <div id="demo" className="carousel slide" data-bs-ride="carousel">
   <div  className="carousel-indicators">
      <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
      <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
      <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
    </div>
    <div  className="carousel-inner">
      <div  className="carousel-item active">
        <img src={img1} alt="image"  className="d-block" />
        <div  className="carousel-caption">
          <h3>Wallet</h3>
          <p>We had such a great experience</p>
        </div>
      </div>
      <div className="carousel-item">
        <img src={img2} alt="image"  className="d-block " />
        <div  className="carousel-caption">
          <h3>Money Transfer</h3>
          <p>Enhancing Digital Money </p>
        </div> 
      </div>
      <div  className="carousel-item">
        <img src={img1} alt="image"  className="d-block"/>
        <div  className="carousel-caption">
          <h3>Future</h3>
          <p>It helps to improve banking</p>
        </div>  
      </div>
    </div>
    
    {/* <!-- Left and right controls/icons --> */}
    <button  className="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
      <span  className="carousel-control-prev-icon"></span>
    </button>
    <button c className="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
      <span  className="carousel-control-next-icon"></span>
    </button>
  </div>

  <div  className="container mt-5">
      <h1  className="text-center">About</h1>
      <div className="row mt-5">
        <div  className="col-md-6">
          <img className="img-fluid" src={img3} alt="machine learning"/>
        </div>
          <div className="col-md-6 mt-4">
            <p  className="text-black"> Digital currency will be the future.
            </p>
          </div>
            </div>
      </div>
    <footer className=" container-fluid ">
    <div className="container">
      <div className="row">
        <div className="col-12">
          <h1> COPYRIGHT CONTENT</h1>

        </div>

      </div>
    </div>

  </footer>
    
   
 </>
  );
}
export default BasicExample; 