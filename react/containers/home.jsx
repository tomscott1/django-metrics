import React from 'react'
import Login from '../login/login'
import { Grid, Row, Col } from 'react-bootstrap'


class Home extends React.Component {
  render() {
    return (
      <div>
        <Grid>
          <Col sm={2} md={3} lg={3} />
          <Col sm={8} md={6} lg={6}>
            {this.props.children}
          </Col>
          <Col sm={2} md={3} lg={3} />
        </Grid>
      </div>
    )
  }
}

export default Home
