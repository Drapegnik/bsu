import Select from "components/Select";
import React, { Component } from 'react';

import InferenceEngine, { mainTarget } from 'core/InferenceEngine';

class GamePage extends Component {
  componentWillMount() {
    this.initState();
  }

  initState = () => this.setState({
    attribute: null,
    options: null,
    context: {},
    finish: false,
  }, this.play);

  play = () => {
    const getContext = () => ({ ...this.state.context });
    const updateContext = (key, value) => this.setState({
      context: { ...this.state.context, [key]: value, }
    });
    const askQuestion = (attribute, options) => {
      this.setState({ attribute, options });
      return new Promise(resolve => {
        this.resolve = resolve;
      })
    };
    const handleFinish = () => this.setState({ finish: true });

    const ie = new InferenceEngine(
      getContext, updateContext, askQuestion, handleFinish
    );
    ie.start();
  };

  handleSelect = value => this.resolve(value);

  render() {
    const { attribute, options, finish, context } = this.state;
    const result = context[mainTarget];

    if (finish) {
      return (
        <div className="container has-text-centered">
          <h1 className="title">
            {result ? `✨You are fun of ${result}!🔥` : 'Sorry, can\'t identify your club 😱('}
          </h1>
          <button onClick={this.initState} className="button is-black is-large">Try Again!</button>
        </div>
      )
    }

    return (
      <div className="container has-text-centered">
        {!attribute && (
          <h1 className="title">Loading...</h1>
        )}
        {attribute && (
          <Select
            attribute={attribute}
            options={options}
            onChange={this.handleSelect}
          />)}
      </div>
    );
  }
}

export default GamePage;
