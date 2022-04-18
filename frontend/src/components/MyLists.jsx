import axios from "axios";
import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

const BookSet = () => {
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
      const books = res.data;
      console.log(lists.data);
      setBooks(lists);
    });
  }, []);

  return (
    <div>
      <center>
        <h1>My Lists</h1>
      </center>
      <Link className="btn btn-dark my-2 my-sm-0 text-light" to="/create">
        Create New List
      </Link>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Number of Books</th>
          </tr>
        </thead>
        <tbody>
          {books && books.map((book, index) => {
            return (
              <tr key={book.isbn}>
                <td>
                    {book.title}
                </td>
                <td>{book.no_of_books}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default BookSet;
