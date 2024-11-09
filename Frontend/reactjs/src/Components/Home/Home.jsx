//@ts-check

import React from "react";
import Post from "../Post/Post";
import "./Home.css"

export default function Home(){
    
    const data = [
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
            {data.map((item) => (
                <Post postData={item} />
            ))}
            </section>
        </main>
    );
}