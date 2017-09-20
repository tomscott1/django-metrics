import React from "react"
import { render } from "react-dom"
import { Route, BrowserRouter } from 'react-router-dom'
import Home from "./containers/home"
import Login from './login/login'
import Register from './login/register'

class IndexContainer extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Route path="/" Component={Home}>
          <Route path="/login" Component={Login} />
          <Route path="/register" Component={Register} />
        </Route>
      </BrowserRouter>
    )
  }
}

render(<IndexContainer/>, document.getElementById('React-Index'))
