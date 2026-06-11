import {

useState

}

from "react";

import api from "../api";


export default function Search(){

const[
query,
setQuery
]=useState("");

const[
results,
setResults
]=useState([]);


const run=
async()=>{

const res=

await api.post(

"/search",

{

text:

query

}

);

setResults(
res.data
);

};


return(

<div>

<input

value={query}

onChange={

e=>

setQuery(
e.target.value
)

}

/>

<button

onClick={run}

>

Search

</button>


{

results.map(

(

r,

i

)=>

<div key={i}>

{r.text}

<br/>

Score:

{r.score}

</div>

)

}

</div>

);

}