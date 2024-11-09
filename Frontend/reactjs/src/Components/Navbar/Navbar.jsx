//@ts-check

import React from "react";
import "./Navbar.css"

export default function NavBar(){
    return (
        <header className="navBar">
            <section>
                <h1>Fundación Escolares</h1>
            </section>

            <ul className="navList">
                <a href="">Home</a>
                <a href="">Registrar</a>
            </ul>
            <hr />
        </header>
    );
}