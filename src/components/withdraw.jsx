import React, { useState } from 'react';
import logo from './logo/cloud.jpg'
import {
  MDBContainer,
  MDBTabs,
  MDBTabsItem,
  MDBTabsLink,
  MDBTabsContent,
  MDBTabsPane,
  MDBBtn,
  MDBIcon,
  MDBInput,
  MDBCheckbox
}
from 'mdb-react-ui-kit';

function Withdraw() {

  const [justifyActive, setJustifyActive] = useState('tab1');;

  const handleJustifyClick = (value) => {
    if (value === justifyActive) {
      return;
    }

    setJustifyActive(value);
  };

  return (

    <MDBContainer className="p-3 my-5 d-flex flex-column w-50">

      <MDBTabs pills justify className='mb-3 d-flex flex-row justify-content-between'>
        <MDBTabsItem>
          <MDBTabsLink onClick={() => handleJustifyClick('tab1')} active={justifyActive === 'tab1'}>
            My Account
          </MDBTabsLink>
        </MDBTabsItem>
        <MDBTabsItem>
          <MDBTabsLink onClick={() => handleJustifyClick('tab2')} active={justifyActive === 'tab2'}>
            Other Account
          </MDBTabsLink>
        </MDBTabsItem>
      </MDBTabs>

      <MDBTabsContent>

        <MDBTabsPane show={justifyActive === 'tab1'}>

         
          <div className="d-flex justify-content-center mx-4 mb-4">
          <label>Amount 
          <MDBInput wrapperClass='mt-4'  id='form1' type='number'/>
          </label> 
           
          </div>
          <div className='d-flex justify-content-center mb-4'>
            <MDBCheckbox name='flexCheck' id='flexCheckDefault' label='Default Account' />
          </div>

          <MDBBtn className="mb-4 w-100">Withdraw</MDBBtn>
          <p className="text-center">Alternate Account? <a href="#!">Other Account</a></p>

        </MDBTabsPane>

        <MDBTabsPane show={justifyActive === 'tab2'}>

          <div className="text-center mb-3">
            <h3><p className="text-center mt-3">Account Details</p></h3>
          </div>

          <MDBInput wrapperClass='mb-4' label='Account number' id='form1' type='number'/>
          <MDBInput wrapperClass='mb-4' label='IFSC' id='form1' type='text'/>
          <MDBInput wrapperClass='mb-4' label='Account holder name' id='form1' type='text'/>
          <MDBInput wrapperClass='mb-4' label='Mobile number' id='form1' type='number'/>
          <MDBInput wrapperClass='mb-4' label='Amount' id='form1' type='number'/>

          <div className='d-flex justify-content-center mb-4'>
            <MDBCheckbox name='flexCheck' id='flexCheckDefault' label='Confirm' />
          </div>

          <MDBBtn className="mb-4 w-100">Withdraw</MDBBtn>

        </MDBTabsPane>

      </MDBTabsContent>

    </MDBContainer>
  );
}

export default Withdraw;