import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let [data, setData] = useState(null)
  function func(){
    return <>{data.map(([coin, prices]) => (
        <div key={coin}>
          <h2>{coin}</h2>
          {prices.map(([currency, value]) => (
            <p key={currency}>
              {currency.toUpperCase()}: {value}
            </p>
          ))}
        </div>
      ))}</>
  }
  
  return (
    <>
      {data != null ? <>{Object.entries(data).map(([coin, prices]) => (
        <div key={coin}>
          <h2>{coin}</h2>
          {Object.entries(prices).map(([currency, value]) => (
            <p key={currency}>
              {currency.toUpperCase()}: {value}
            </p>
          ))}
        </div>
      ))}</> : <></> }
      <button onClick={() => {
        fetch("http://localhost:8080/", {
          headers:{
            "Content-Type": "application/json"
          },
        }).then(data => data.json())
        .then(res => { 
          setData(res); 
          console.log(res); 
          })
      }}>Click me!</button>
        
    </>
  );
}

export default App;
