import React from "react";
import logo from './logo/cloud.jpg'

function C_home(){
    return(
        <>
        {/* navbar */}
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
                                    <img src="" alt="balance" className="edit"/>MY BALANCE
                                </button>

                            </a>

                        </li>
                        <li className="navbar-nav">
                            <a className="nav-link" href="">
                                <button>
                                    <img src="" alt="balance" className="edit"/>MY ACCOUNT
                                </button>

                            </a>

                        </li>
                        <li className="navbar-nav">
                            <a className="nav-link" href="">
                                <button>
                                    <img src="" alt="balance" className="edit"/>HELP ?
                                </button>

                            </a>

                        </li>
                    </ul>

                </div>

            </div>

        </nav>

        {/* navbar */}


        {/* body */}

        <h2 className="text-center" style={{marginTop:'8%'}}>Welcome to cloud pay wallet</h2>
        <div className="justify-content-center d-flex" style={{marginBottom:'5%'}}>
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src="" alt="logo"/><a href="" style={{textDecoration:"none"}}>ADD MONEY</a></button>
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src="" alt="logo"/><a href="" style={{textDecoration:"none"}}>WITHDRAW</a></button>
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src="" alt="logo"/><a href="" style={{textDecoration:"none"}}>SEND</a></button>

        </div>






        </>

    );
}

export default C_home;
