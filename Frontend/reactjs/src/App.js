import './App.css';
import { useState } from 'react';
import NavBar from './Components/Navbar/Navbar.jsx';
import Home from './Components/Home/Home.jsx';
import Registrar from './Components/Registrar/Registrar.jsx';
import Ingresar from './Components/Ingresar/Ingresar.jsx';

function App() {
  const [page, setPage] = useState("home");

  const renderPage = () => {
    switch (page) {
      case "home":
        return <Home/>;
      case "registrar":
        return <Registrar/>
      case "ingresar":
        return <Ingresar />;
      default:
        return <Home />;
    }
  };

  return (
    
    <body> 
        <header className="navBar">
          <section>
              <h1>Fundación Escolares</h1>
          </section>

          <nav>
            <button onClick={() => setPage("home")}>Home</button>
            <button onClick={() => setPage("registrar")}>Registrar</button>
            <button onClick={() => setPage("ingresar")}>Ingresar</button>
          </nav> 
          <hr />
        </header>
      {renderPage()}
    </body>
  );
}

export default App;
