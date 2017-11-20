import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Select extends Component {
  static propTypes = {
    attribute: PropTypes.string.isRequired,
    options: PropTypes.arrayOf(
      PropTypes.string.isRequired
    ).isRequired,
    onChange: PropTypes.func.isRequired
  };

  render() {
    const { attribute, options, onChange } = this.props;

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
              value={''}
              onChange={({ target }) => onChange(target.value)}
            >
              <option>...</option>
              {options.map(value => (
                <option key={value} value={value}>{value}</option>
              ))}
            </select>
          </div>
        </div>
      </div>
    );
  }
}

export default Select;
