//@ts-check


import React from "react";
import Post from "../Post/Post";
import axios from "axios";
import "./Home.css"
import { useState, useEffect } from "react";


export default function Home(){
    
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios
          .get('/') // Replace with your API URL
          .then((response) => {
            setData(response.data);
            setLoading(false);
          })
          .catch((error) => {
            console.log(error)
          });
      }, []);

    const oldata = [
        {
            title: "t1",
            body: "b1",
            userId: "u1",
            schoolId: "s1"
        },
        {
            title: "t2",
            body: "b2",
            userId: "u2",
            schoolId: "s2"
        },
        {
            title: "t3",
            body: "b3",
            userId: "u3",
            schoolId: "s3"
        },
        {
            title: "t4",
            body: "b4",
            userId: "u4",
            schoolId: "s4"
        }
    ]

    
    return (
        <main>
            <section>
            <p>{data}</p>
            </section>
        </main>
    );
}