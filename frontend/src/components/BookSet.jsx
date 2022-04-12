import axios from "axios";
import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

const BookSet = () => {
  const [books, setBooks] = useState([]);

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
    axios.get("http://localhost:8000/api/books").then((res) => {
      const books = res.data;
      setBooks(books.data);
    });
  }, []);

  return (
    <div>
      <center>
        <h1>Book List</h1>
      </center>
      <Link className="btn btn-dark my-2 my-sm-0 text-light" to="/create">
        Create New Book
      </Link>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">ISBN</th>
            <th scope="col">Title</th>
            <th scope="col">Summary</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody>
          {books && books.map((book, index) => {
            return (
              <tr key={book.ID}>
                <th>{index + 1}</th>
                <td>
                  <Link key={book.ID} to={`/api/books/${book.ID}`}>
                    {book.Title}
                  </Link>
                </td>
                <td>{book.Summary}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default BookSet;
