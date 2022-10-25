import React, { useState } from "react";
import "./App.css";
// import DisplayContent from './DisplayContent';
import Search from "./component/Search";
import Borrow from "./component/Borrow";
import Return from "./component/Return";
import Add from "./component/Add";
function App() {
    const [searchState, setSearchState] = useState(true);
    const [borowState, setBorrowState] = useState(false);
    const [returnState, setReturnState] = useState(false);
    const [addState, setAddState] = useState(false);

    function clickSearch() {
        setSearchState(true);
        setBorrowState(false);
        setReturnState(false);
        setAddState(false);
    }

    function clickBorrow() {
        setSearchState(false);
        setBorrowState(true);
        setReturnState(false);
        setAddState(false);
    }

    function clickReturn() {
        setSearchState(false);
        setBorrowState(false);
        setReturnState(true);
        setAddState(false);
    }

    function clickAdd() {
        setSearchState(false);
        setBorrowState(false);
        setReturnState(false);
        setAddState(true);
    }

    function torender() {
        if (searchState) {
            return <Search />
        } else if (borowState) {
            return <Borrow />
        } else if (returnState) {
            return <Return />
        } else if (addState) {
            return <Add />
        }
    }

    return (
        <div>
            <nav>
                <ul className="top-list">
                    <li>
                        <button onClick={clickSearch}> Search</button>
                    </li>
                    <li>
                        <button onClick={clickBorrow}> Borrow</button>
                    </li>
                    <li>
                        <button onClick={clickReturn}> Return</button>
                    </li>
                    <li>
                        <button onClick={clickAdd}> Add</button>
                    </li>
                </ul>
            </nav>
            <div>
                {torender()}
            </div>
            
        </div>





        
    );
}

export default App;
