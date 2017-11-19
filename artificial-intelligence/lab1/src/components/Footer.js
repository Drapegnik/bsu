import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';

const routes = [{
  key: 'welcome',
  label: 'Overview',
}, {
  key: 'game',
  label: 'Play',
}, {
  key: 'knowledge',
  label: 'Knowledge base',
}];

const Footer = ({ activeRoute, onRouteChange }) => (
  <div className="hero-foot">
    <nav className="tabs is-boxed is-fullwidth">
      <div className="container">
        <ul>
          {routes.map(({ key, label }) => (
            <li key={key} className={classNames({ 'is-active': key === activeRoute })}>
              <a onClick={onRouteChange.bind(null, key)}>{label}</a>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  </div>
);

Footer.propTypes = {
  activeRoute: PropTypes.string.isRequired,
  onRouteChange: PropTypes.func.isRequired
};

export default Footer;
