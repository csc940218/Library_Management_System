import React, { useState } from "react";
import Result from "./Result";

function Search() {
    const [search, setSearch] = useState("");
    const [return_data, setReturn_data] = useState("");
    const [searchurl, setSearchurl] = useState("http://127.0.0.1:5000/");

    function keywordButtonClickHander(){
        setSearchurl("http://127.0.0.1:5000/search/keyword?keyword=")
    }

    function ISBNButtonClickHander(){
        setSearchurl("http://127.0.0.1:5000/search/ISBN13?ISBN13=")
    }

    function createEntry(Record_obj) {
        return (
          <Result
          key={Record_obj.ISBN13}
            ISBN13={Record_obj.ISBN13}
            title={Record_obj.title}
            availiability={Record_obj.availiability}
            total={Record_obj.total}
          />
        );
      }

    function changehandler(e) {
        setSearch(e.target.value);
    }

    function submithandler(e) {
        e.preventDefault();
        const searchcriteria = search;

        var finalurl = searchurl.concat(searchcriteria);
        getresponse()


        async function getresponse() {
            const response = await fetch(finalurl);
            const data = await response.json();
            setReturn_data(data);
        }



    }


    





    return (
        <div>
            <form  id="ISBN" className="keyword" onSubmit={submithandler}>
                <input
                    onChange={changehandler}
                    defaultValue={search}
                    name="search"
                    id="name"
                    placeholder="Keyword/ISBN13"
                    required
                ></input>
                <br></br>
                <button
                    className="keyword"
                    type="submit"
                    onClick={keywordButtonClickHander}
                >
                    Search by Keyword
                </button>
                <button
                    className="ISBN13"
                    type="submit"
                    onClick={ISBNButtonClickHander}
                >
                    Search by ISBN
                </button>
            </form>
            <div>
                {return_data.message &&  <p>{return_data.message}</p> }
                </div>
            <div id="flex">
                {return_data[0] && return_data.map(createEntry)}
            </div>
        </div>
    );
}

export default Search;
