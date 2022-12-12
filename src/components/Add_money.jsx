import React from "react";
import logo from './logo/cloud.jpg'
import addmoney from "../API_connection/addmoney";



function Money(){
    const onFinish =async(values) =>{
        const userdata={
            Add:values.card,
            expiry:values.card,
            CVV:values.cvv,
            Amount:values.amount,
            Mobile_number:values.number,
            save_details:values.remember
        };
        const response =await addmoney(userdata);
    }
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
           <div className="container mt-3">
            <div className="card">
                <div className="card-header">ADD CARD DETAILS</div>


                <div className="card-body">
                    <form action="/">
                        <div className="mb-3 mt-3">
                           
                            <input type="number" className="form-control"  id="" name="card" placeholder="enter the valid card number"/>

                        </div>
                       <div className="row">
                        <div className="col">
                            <div className=""mb-3 mt-3>
                                
                                <input type="date" className="form-control"  id=""  placeholder="mm/yy" name="expiry"/>

                            </div>

                        </div>
                        <div className="col">
                            <div className="mb-3">
                                
                                <input type="number" className="form-control" data-mask="000"  id="" placeholder="cvv" name="cvv"/>

                            </div>

                        </div>


                       </div>
                       <div className="mb-3 mt-3">
                       <input type="number" className="form-control"   id="" placeholder="amount" name="amount"/>
                       </div>
                       <div className="mb-3 mt-3">
                       <input type="number" className="form-control" name="number" id="" placeholder="mobile number" />
                       </div>
                       <div className="">
                       <div className="form-check mb-3">
                        <label className="form-check-label">
                            <input className="form-check-input" type="checkbox" name="remember"/>Save card details

                        </label>

                       </div>

                       <input className="btn btn-secondary" type="reset"/>
                       <a className="btn btn-primary" href="#" role="button" onClick={onFinish}>Process</a>
                       </div>



                    </form>

                </div>

            </div>

           </div>









        {/* body */}
        
        </>
    );
}
export default Money;