import axios from "axios";
import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

const MyLists = () => {
  const [lists, listBooks] = useState([]);

  /*
  const onDelete = (id) => {
    axios
      .delete(`problem/delete/${id}`)
      .then((res) => {
        axios.get("http://localhost:8080/problem/view").then((res) => {
          const questions = res.data;
          setProblems(questions.data);
        });
      })
      .catch((err) => console.log(err));
  };
  */

  useEffect(() => {
    axios.get("http://localhost:8000/lists").then((res) => {
      const lists = res.data;
      console.log(lists);
      listBooks(lists);
    });
  }, []);

  return (
    <div style={{color: "white"}}>
      <center>
        <h1>My Lists</h1>
      </center>
      <table className="table" style={{color: "white"}}>
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">List Name</th>
            <th scope="col">ISBN</th>
          </tr>
        </thead>
        <tbody>
          {lists && lists.map((book, index) => {
            return (
              <tr key={book.isbn_id}>
                <th>{index + 1}</th>
                <td>
                    {book.listName}
                </td>
                <td>{book.isbn_id}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default MyLists;
