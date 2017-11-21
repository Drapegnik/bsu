import React, { Component } from 'react';

import KnowledgeBase from 'components/KnowledgeBase';
import Select from 'components/Select';

import InferenceEngine from 'core/InferenceEngine';

import { targets } from 'data';

class GamePage extends Component {
  state = {
    attribute: null,
    mainTarget: null,
    context: {},
  };

  play = () => this.setState({
    attribute: null,
    options: null,
    context: {},
    logs: [],
    finish: false,
  }, this.startAlgo);

  startAlgo = () => {
    const getContext = () => ({ ...this.state.context });
    const updateContext = (key, value) => this.setState({
      context: { ...this.state.context, [key]: value },
    });
    const askQuestion = (attribute, options) => {
      this.setState({ attribute, options });
      return new Promise((resolve) => {
        this.resolve = resolve;
      });
    };
    const handleFinish = () => this.setState({ finish: true });
    const log = rule => this.setState({ logs: this.state.logs.concat(rule) });

    const ie = new InferenceEngine(
      this.state.mainTarget,
      getContext,
      updateContext,
      askQuestion,
      handleFinish,
      log
    );
    ie.start();
  };

  handleSelect = value => this.resolve(value);

  handleTargetChange = target => this.setState({ mainTarget: target }, this.play);

  render() {
    const {
      attribute, options, finish, context, logs, mainTarget
    } = this.state;
    const result = context[mainTarget];

    return (
      <div className="container has-text-centered">
        <Select
          label="Select target"
          value={mainTarget || ""}
          options={targets}
          onChange={this.handleTargetChange}
        />
        <br />
        {finish && (
          <div>
            <h1 className="title">
              {result ? `✨Your target is ${result}!🔥` : 'Sorry, can\'t identify your target 😱('}
            </h1>
            <button onClick={this.play} className="button is-black is-large">Try again!</button>
          </div>
        )}
        {mainTarget && attribute && !finish && (
          <Select
            value=""
            label={`Choose ${attribute} of your target:`}
            attribute={attribute}
            options={options}
            onChange={this.handleSelect}
          />)}
        <br />
        {logs && (
          <KnowledgeBase rules={logs} />
        )}
      </div>
    );
  }
}

export default GamePage;
