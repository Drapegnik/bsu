import React, { Component } from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';

import Input from './components/Input';
import { post, api } from './utils';

global.XMLHttpRequest = global.originalXMLHttpRequest || global.XMLHttpRequest;

export default class App extends Component {
  state = {
    p: '61',
    q: '53',
    user: 'admin',
    publicKey: null,
    privateKey: null,
    sessionKey: null,
    rsaOpened: false,
    text: null,
  };

  handleError = error => {
    console.error(error);
    if (error.code && error.code === 401) {
      this.setState({
        sessionKey: null,
        error: error.message,
      });
      return;
    }
    this.setState({ error });
  };

  handleRsaSectionTogle = () => this.setState({ rsaOpened: !this.state.rsaOpened, error: null });

  generateKeys = () => {
    const { p, q } = this.state;
    post(api.private.rsaGenerate, { p, q })
      .then(({ e, n, d }) => {
        this.setState({
          sessionKey: null,
          publicKey: { e, n },
          privateKey: { d, n },
          rsaOpened: false,
          error: null,
        });
      })
      .catch(this.handleError);
  };

  login = () => {
    const { user, publicKey, privateKey } = this.state;
    post(api.login, { user, key: publicKey })
      .then(({ sessionKey }) => {
        console.log('encrypted sessionKey: ', sessionKey);
        return post(api.private.rsaDecrypt, { key: privateKey, data: sessionKey });
      })
      .then(({ decrypted }) => {
        console.log('decrypted sessionKey: ', decrypted);
        this.setState({
          sessionKey: decrypted,
        });
      })
      .catch(this.handleError);
  };

  getData = () => {
    const { user, sessionKey: key } = this.state;
    post(api.getData, { user })
      .then(({ text }) => {
        console.log('encrypted text: ', text);
        return post(api.private.aesDecrypt, { key, data: text });
      })
      .then(({ text }) => this.setState({ text }))
      .catch(this.handleError);
  };

  render() {
    const { error, rsaOpened, publicKey, privateKey, sessionKey, text } = this.state;
    const hasRsa = publicKey && privateKey;

    return (
      <View style={styles.container}>
        {error && <Text style={{ color: 'red' }}>{error}</Text>}
        {hasRsa && (
          <View>
            <Text>DATA:</Text>
            <Text>
              Public: ({publicKey.e}, {publicKey.n})
            </Text>
            <Text>
              Private: ({privateKey.d}, {privateKey.n})
            </Text>
            {sessionKey && <Text>Session: {sessionKey}</Text>}
          </View>
        )}
        <Button
          onPress={this.handleRsaSectionTogle}
          title={`${hasRsa ? 'Reg' : 'G'}enerate rsa keys`}
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
        {hasRsa && !rsaOpened && !sessionKey && <Button onPress={this.login} title="Login" />}
        {sessionKey && <Button onPress={this.getData} title="Get data" />}
        {text && <Text>{text}</Text>}
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
