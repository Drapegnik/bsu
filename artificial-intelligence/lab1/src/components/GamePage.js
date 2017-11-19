import Select from "components/Select";
import React, { Component } from 'react';
import PropTypes from 'prop-types';

class GamePage extends Component {
  static propTypes = {};

  state = {
    attribute: 'city',
    context: {}
  };

  handleSelect = value => {
    const { attribute, context } = this.state;
    this.setState({
      context: {
        ...context,
        [attribute]: value,
      }
    })
  };

  render() {
    const { attribute } = this.state;

    return (
      <div className="container has-text-centered">
        <Select
          attribute={attribute}
          onSubmit={this.handleSelect}
        />
      </div>
    );
  }
}

export default GamePage;
