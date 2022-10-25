import React, { useState } from "react";

function Borrow() {
    const borrowurl = "http://127.0.0.1:5000/Borrow";
    const [ISBN13, setISBN13] = useState("");
    const [username, setusername] = useState("");
    const [password, setpassword] = useState("");
    const [return_data, setReturn_data] = useState("");

    function ISBNchangehandler(e) {
        setISBN13(e.target.value);
    }

    function usernamechangehandler(e) {
        setusername(e.target.value);
    }

    function passwordchangehandler(e) {
        setpassword(Number(e.target.value));
    }

    function borrowsubmithandler(e) {
        e.preventDefault();
        const borrow_boject = { ISBN13, username, password };
        getresponse(borrow_boject);

        async function getresponse(borrow_boject) {
            const response = await fetch(borrowurl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(borrow_boject),
            });

            const return_message = await response.json();
            setReturn_data(return_message);
        }
    }

    return (
        <div>
            <form onSubmit={borrowsubmithandler}>
                <input
                    onChange={ISBNchangehandler}
                    value={ISBN13}
                    name="search"
                    type=""
                    id="ISBN13"
                    placeholder="ISBN13"
                    required
                    pattern="[0-9]{13}"
                ></input>
                <br></br>
                <input
                    onChange={usernamechangehandler}
                    value={username}
                    name="search"
                    type=""
                    id="Username"
                    placeholder="username"
                    required
                    maxLength="10"
                ></input>
                <br></br>
                <input
                    onChange={passwordchangehandler}
                    value={password}
                    name="search"
                    type="password"
                    id="name"
                    placeholder="password"
                    required
                    pattern="[0-9]+"
                ></input>
                <br></br>
                <button  type="">
                    Borrow{" "}
                </button>
            </form>
            <div id="return_message">
                {return_data.message && <p>{return_data.message}</p>}
            </div>
        </div>
    );
}

export default Borrow;
