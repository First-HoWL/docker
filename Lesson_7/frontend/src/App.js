import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import {  Route, Routes, useNavigate, useParams } from 'react-router';

function IndexPage(){
  let [data, setData] = useState(null)
  
  useEffect(() => {
    fetch("http://localhost:8080/", {
          headers:{
            "Content-Type": "application/json"
          },
        }).then(data => data.json()).then(resp => setData(resp))
  }, [])

  return(<>
      {data != null ? <>{data}</> : <>Loading...</> }
      <button onClick={() => {
        
      }}>Edit!</button>
  </>)
}
function EditPage(){
  const [data, setData] = useState()
  return (
    <>
    <form onSubmit={
      fetch(`http://localhost:8080/edit/${data}`, {
          headers:{
            "Content-Type": "application/json"
          },
        })
        
    }>
      <input type='text' placeholder='message of the day' value={data} onChange={(e)=> setData(e.target.value)}></input>
      <button type="submit"></button>
    </form>
    </>
  )
}


function App() {

  

  return (
    <>
    <Routes>
      <Route path='/' element={<IndexPage />} />
      <Route path='/edit' element={<EditPage />} />
    </Routes>
      
        
    </>
  );
}

export default App;
