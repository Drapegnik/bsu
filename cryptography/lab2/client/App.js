import React, { Component } from 'react';
import { Alert, StyleSheet, Text, View, Button, TextInput } from 'react-native';

import Input from './components/Input';
import { post } from './utils';

global.XMLHttpRequest = global.originalXMLHttpRequest || global.XMLHttpRequest;

export default class App extends Component {
  state = {
    p: '61',
    q: '53',
    publicKey: null,
    privateKey: null,
    rsaOpened: false,
  };

  handleRsaSectionTogle = () => this.setState({ rsaOpened: !this.state.rsaOpened });

  generateKeys = () => {
    const { p, q } = this.state;
    post('private/rsa/generate', { p, q }).then(({ data: { e, n, d } }) => {
      this.setState({
        publicKey: { e, n },
        privateKey: { d, n },
        rsaOpened: false,
      });
    });
  };

  render() {
    const { rsaOpened, publicKey, privateKey } = this.state;

    return (
      <View style={styles.container}>
        {publicKey &&
          privateKey && (
            <View>
              <Text>rsa keys:</Text>
              <Text>
                Public: ({publicKey.e}, {publicKey.n})
              </Text>
              <Text>
                Private: ({privateKey.d}, {privateKey.n})
              </Text>
            </View>
          )}
        <Button
          onPress={this.handleRsaSectionTogle}
          title={`${publicKey && privateKey ? 'Reg' : 'G'}enerate rsa keys`}
        />
        {rsaOpened && (
          <View>
            <Input
              label="pass prime p:"
              value={this.state.p}
              onChange={p => this.setState({ p })}
            />
            <Input
              label="pass prime q:"
              value={this.state.q}
              onChange={q => this.setState({ q })}
            />
            <Button onPress={this.generateKeys} title="Submit" />
          </View>
        )}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
});
