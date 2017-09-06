import React from "react"
import { render } from "react-dom"

import Home from "./containers/home"

class IndexContainer extends React.Component {
  render() {
    return (
      <Home />
    )
  }
}

render(<IndexContainer/>, document.getElementById('React-Index'))
