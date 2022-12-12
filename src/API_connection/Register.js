import axios from "axios";
const Registerdata =async (userdata) => {
    let res={};
    const url='http://localhost:3333/Register';
    try{
        const response =await axios.post(url,userdata);
        res.message= response.data.message;
        return res;
    }
    catch(err){
        res.error=err.response.data;
    }
};


export default Registerdata;
