import React from 'react';
import PropTypes from 'prop-types';

const Select = ({ label, options, onChange, value }) => (
  <div className="field has-addons has-addons-centered">
    <div className="control">
      <button className="button is-black is-large">
        {label}
      </button>
    </div>
    <div className="control">
      <div className="select is-black is-large">
        <select
          value={value}
          onChange={({ target }) => onChange(target.value)}
        >
          <option>...</option>
          {options.map(value => (<option key={value} value={value}>{value}</option>))}
        </select>
      </div>
    </div>
  </div>
);

Select.propTypes = {
  options: PropTypes.arrayOf(PropTypes.string.isRequired).isRequired,
  onChange: PropTypes.func.isRequired,
};

export default Select;
