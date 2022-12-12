import './App.css';
import BasicExample from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import C_home from './components/cloudpay_home';
import Money from './components/Add_money';
import withdraw from './components/withdraw';
import {Route,Routes ,BrowserRouter as Router} from "react-router-dom";
import Withdraw from './components/withdraw';
import Send from './components/sendmoney';

function App() {
  return (
    <Router>
    <div className="App">
      <Routes>
        <Route path='/' element={<BasicExample/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/cloud' element={<C_home/>}/>
        <Route path='/add' element={<Money/>}/>
        <Route path='/minus' element={<Withdraw/>}/>
        <Route path='/send'  element={<Send/>}/>
      </Routes>
     
    </div>
    </Router>
  );
}

export default App;
