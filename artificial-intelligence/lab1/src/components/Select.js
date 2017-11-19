import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Select extends Component {
  static propTypes = {
    attribute: PropTypes.string.isRequired,
    options: PropTypes.arrayOf(
      PropTypes.string.isRequired
    ).isRequired,
    onSubmit: PropTypes.func.isRequired
  };

  state = {
    value: null
  };

  render() {
    const { attribute, onSubmit } = this.props;
    const { value } = this.state;

    return (
      <div className="field has-addons has-addons-centered">
        <div className="control">
          <button className="button is-black is-large">
            Choose {attribute} of your club:
          </button>
        </div>
        <div className="control">
          <div className="select is-black is-large">
            <select
              value={value}
              onChange={({ target }) => this.setState({ value: target.value })}
            >
              {!value && (<option>...</option>)}
              <option>London</option>
              <option>Liverpool</option>
              <option>Manchester</option>
              <option>Other</option>
            </select>
          </div>
        </div>
        <div className="control">
          <button
            className="button is-black is-large"
            type="submit"
            disabled={!value}
            onClick={onSubmit.bind(null, value)}
          >
            Next
          </button>
        </div>
      </div>
    );
  }
}

export default Select;
