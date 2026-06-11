import {

useState

}

from "react";

import api from "../api";


export default function Upload(){

const[
text,
setText
]=useState("");


const submit=
async()=>{

await api.post(

"/upload",

{

text

}

);

alert(
"Uploaded"
);

};


return(

<div>

<textarea

rows="8"

value={text}

onChange={

e=>

setText(
e.target.value
)

}

/>

<button

onClick={submit}

>

Upload

</button>

</div>

);

}