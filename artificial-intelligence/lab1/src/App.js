import React, { Component } from 'react';

import WelcomePage from 'components/WelcomePage';
import GamePage from 'components/GamePage';
import KnowledgeBase from 'components/KnowledgeBase';
import Footer from 'components/Footer';

import 'bulma/css/bulma.css';
import 'App.css';

const pages = {
  'welcome': <WelcomePage />,
  'game': <GamePage />,
  'knowledge': <KnowledgeBase />,
};

class App extends Component {
  state = {
    route: 'welcome',
  };

  changeRoute = route => this.setState({ route });

  render() {
    const { route } = this.state;

    return (
      <section className="hero is-primary is-bold is-fullheight">
        <div className="hero-body">
          {pages[route]}
        </div>
        <Footer activeRoute={route} onRouteChange={this.changeRoute} />
      </section>
    );
  }
}

export default App;
