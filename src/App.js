import './App.css';
import BasicExample from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import {Route,Routes ,BrowserRouter as Router} from "react-router-dom";

function App() {
  return (
    <Router>
    <div className="App">
      <Routes>
        <Route path='/' element={<BasicExample/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Register/>}/>
      </Routes>
     
    </div>
    </Router>
  );
}

export default App;
