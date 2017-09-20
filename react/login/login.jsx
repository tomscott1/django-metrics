import React from 'react'
import { FormGroup, FormControl, ControlLabel, Grid, Row, Col } from 'react-bootstrap'

class Login extends React.Component {
  render() {
    return (
      <div>
        <FormGroup>
          <ControlLabel>
            Username:
          </ControlLabel>
          <FormControl
            type="text"
            placeholder="Enter username"
          />
        </FormGroup>
        <FormGroup>
          <ControlLabel>
            Password:
          </ControlLabel>
          <FormControl
            type="text"
            placeholder="Enter password"
          />
        </FormGroup>
        No Account? <a href="#">Register Here</a>
      </div>
    )
  }
}

export default Login
