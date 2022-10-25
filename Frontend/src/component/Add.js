import React,{useState} from "react";

function Add() {



    const borrowurl = "http://127.0.0.1:5000/Add";
    const [ISBN13, setISBN13] = useState("");
    const [title, setTitle] = useState("");
    const [quantity, setQuantity] = useState("");
    const [username, setusername] = useState("");
    const [password, setpassword] = useState("");
    const [return_data, setReturn_data] = useState("");

    function ISBNchangehandler(e) {
        setISBN13(e.target.value);
    }
    function titlechangehandler(e) {
        setTitle(e.target.value);
    }
    function quantitychangehandler(e) {
        setQuantity(Number(e.target.value));
    }

    function usernamechangehandler(e) {
        setusername(e.target.value);
    }

    function passwordchangehandler(e) {
        setpassword(Number(e.target.value));
    }

    function addsubmithandler(e) {
        e.preventDefault();
        const add_boject = { ISBN13, title,quantity, username, password };
        getresponse(add_boject);

        async function getresponse(add_boject) {
            const response = await fetch(borrowurl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(add_boject),
            });

            const return_message = await response.json();
            setReturn_data(return_message);
        }
    }
























        return (
            <div>
                <form onSubmit={addsubmithandler}id="add">
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
                    onChange={titlechangehandler}
                    value={title}
                        name="search"
                        type=""
                        id="title"
                        placeholder="Title"
                        required
                        maxLength="1000"
                    ></input>
                    <br></br>
                    <input
                    onChange={quantitychangehandler}
                    value={quantity}
                        name="search"
                        type="number"
                        id="Quantity"
                        placeholder="Quantity"
                        required
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
                    <button  type="">Add </button>
                </form>

                <div id="return_message">
                {return_data.message && <p>{return_data.message}</p>}
            </div>
            </div>
        );
    } 

export default Add;
