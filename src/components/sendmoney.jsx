import React from "react";
import logo from './logo/cloud.jpg'
import help from './logo/help.jpg'
import rupee from './logo/currency-symbol.jpg'




function Send(){
    return(
        <>
        <nav className="navbar navbar-expand-sm justify-content-end p-0 bg-light">
        <div className="container-fluid">
            <a className="navbar-brand" href="#">
                <div className="btn btn-light">
                    <h5><img src={logo} alt="" width={'50px'}/>Cloud pay</h5>

                </div>
            </a>
            <div className="justify-content-end">
                <ul className="nav">
                <li className="navbar-nav">
                            <a className="nav-link" href="">
                                <button className="button">
                                    <img src={rupee} alt="balance" width={'45px'} className="edit"/>MY BALANCE
                                </button>

                            </a>

                        </li>
                   
                    <li className="navbar-nav">
                        <a className="nav-link" href="">
                            <button>
                                <img src={help} width={'50px'} alt="balance" className="edit"/>HELP ?
                            </button>

                        </a>

                    </li>
                </ul>

            </div>

        </div>

    </nav>


     <h2 className="text-center" style={{marginTop:'3%'}}> Send Money</h2>
     <div className="container">
        <div className="row justify-content-center">
        <form action="" className="form-control" style={{"width":500}} >
            Email: <input type="email" className="form-control"/>
            Amount: <input type="number" className="form-control"/>
       
        <textarea className="my-3" rows="4" style={{"width":450}} placeholder="Message">

        </textarea>
        <button className="mb-4 w-50">Send</button>
        

        </form>
        </div>
       

     </div>

        
     </>
    );

}

export default Send;