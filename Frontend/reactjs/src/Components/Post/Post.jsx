//@ts-check

import React from "react";
import "./Post.css"

export default function Post({postData}){
    return (
        <article>
            <section>
                <h1>{postData.title}</h1>
            </section>
            <p>------------</p>
            <section>
                <div>
                    <p>{postData.schoolId}</p>
                    <p>{postData.userId}</p>
                </div>
                <div>
                    <p>{postData.body}</p>
                </div>
            </section>
        </article>
    );
}