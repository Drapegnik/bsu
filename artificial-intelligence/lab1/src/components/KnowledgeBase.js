import React from 'react';
import PropTypes from 'prop-types';

import { rules as initialRules } from 'data';

const Keyword = ({ label }) => (
  <div className="control">
    <div className="tags">
      <strong>{label}</strong>
    </div>
  </div>
);
Keyword.propTypes = { label: PropTypes.string.isRequired };

const KeyValue = ({ attr, value, showAnd, alt }) => (
  <div className="control">
    <div className="field is-grouped is-grouped-multiline">
      <div className="control">
        <div className="tags has-addons">
          <span className={`tag is-${alt ? 'black' : 'dark'}`}>{attr}</span>
          <span className={`tag is-${alt ? 'info' : 'white'}`}>{value}</span>
        </div>
      </div>
      {showAnd && (<Keyword label="AND" />)}
    </div>
  </div>
);

KeyValue.propTypes = {
  attr: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  showAnd: PropTypes.bool,
  alt: PropTypes.bool,
};

KeyValue.defaultProps = {
  showAnd: false,
  alt: false,
};

const KnowledgeBase = ({ rules }) => (
  <div className="container">
    <ul>
      {rules.map(rule => (
        <li className="level" key={rule.id}>
          #{rule.id}
          <div className="field is-grouped is-grouped-multiline">
            <Keyword label="IF" />
            {rule.if.map(({ attr, value }, index) => (
              <KeyValue
                key={attr}
                attr={attr}
                value={value}
                showAnd={index !== rule.if.length - 1}
              />
            ))}
            <Keyword label="THEN" />
            <KeyValue attr={rule.then.attr} value={rule.then.value} alt />
          </div>
        </li>
      ))}
    </ul>
  </div>
);

KnowledgeBase.propTypes = { rules: PropTypes.array, };

KnowledgeBase.defaultProps = { rules: initialRules, };

export default KnowledgeBase;
