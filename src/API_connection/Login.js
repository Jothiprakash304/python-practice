import axios from "axios";

const Logindata= async(login_detail)=>{
    let res={};
    const url='http://localhost:3333/login';
    try{
        const response=await axios.post(url,login_detail);
        res.message=response.data.message;
        return res
    }
    catch(err){
        res.error=err.response.data
    }
};
export default Logindata;