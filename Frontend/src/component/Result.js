import React from "react";

function Result(props) {
    return (
        <div id="box">
            <div>ISBN13:{props.ISBN13}</div>
            <div>Title:{props.title}</div>
            <div>Availiability: {props.availiability}</div>
            <div>Total: {props.total}</div>
        </div>
    );
}
export default Result;
