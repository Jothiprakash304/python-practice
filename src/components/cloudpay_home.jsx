import React from "react";
import logo from './logo/cloud.jpg'
import hello from './logo/withdraw.jpg'
import help from './logo/help.jpg'
import rupee from './logo/currency-symbol.jpg'
import amount from './logo/add-money.jpg'
import account from './logo/account.jpg'
import money from './logo/money.jpg'

import './cloud.css';

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
                                    <img src={rupee} alt="balance" width={'50px'} className="edit"/>MY BALANCE
                                </button>

                            </a>

                        </li>
                        <li className="navbar-nav">
                            <a className="nav-link" href="">
                                <button>
                                    <img src={account} alt="balance"  width={'50px'} className="edit"/>MY ACCOUNT
                                </button>

                            </a>

                        </li>
                        <li className="navbar-nav">
                            <a className="nav-link" href="">
                                <button>
                                    <img src={help} alt="balance" width={'50px'} className="edit"/>HELP ?
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
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src={amount} width={'30px'} alt="logo"/><a href="" style={{textDecoration:"none"}}>ADD MONEY</a></button>
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src={hello} width={'35px'} alt="logo"/><a href="" style={{textDecoration:"none"}}>WITHDRAW</a></button>
            <button style={{width:"140px",height:"50px",borderRadius:"3px"}} className="mx-4 raise"><img className="change" src={money} width={'35px'} alt="logo"/><a href="" style={{textDecoration:"none"}}>SEND</a></button>

        </div>






        </>

    );
}

export default C_home;
