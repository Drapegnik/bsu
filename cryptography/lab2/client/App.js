import React, { Component } from 'react';
import { StyleSheet, Text, View, Button, TextInput, ScrollView } from 'react-native';

import DataView from './components/DataView';
import NumberInput from './components/NumberInput';
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
    if (error.code && error.code === 401) {
      this.setState({
        sessionKey: null,
        error: error.message,
      });
      return;
    }
    this.setState({ error });
  };

  handleRsaSectionTogle = () => {
    this.setState({
      rsaOpened: !this.state.rsaOpened,
      error: null,
    });
  };

  generateKeys = async () => {
    try {
      const { p, q } = this.state;
      const { e, n, d } = await post(api.private.rsaGenerate, { p, q });
      this.setState({
        text: null,
        sessionKey: null,
        publicKey: { e, n },
        privateKey: { d, n },
        rsaOpened: false,
        error: null,
      });
    } catch (err) {
      this.handleError(err);
    }
  };

  login = async () => {
    try {
      const { user, publicKey, privateKey } = this.state;
      const { sessionKey } = await post(api.login, { user, key: publicKey });
      console.log('encrypted sessionKey: ', sessionKey);

      const { decrypted } = await post(api.private.rsaDecrypt, {
        key: privateKey,
        data: sessionKey,
      });
      console.log('decrypted sessionKey: ', decrypted);
      this.setState({ sessionKey: decrypted });
    } catch (err) {
      this.handleError(err);
    }
  };

  getData = async () => {
    try {
      const { user, sessionKey: key } = this.state;
      const { encrypted } = await post(api.getData, { user });
      console.log('encrypted: ', encrypted);

      const { text } = await post(api.private.aesDecrypt, { key, encrypted });
      this.setState({ text, rsaOpened: false });
    } catch (err) {
      this.handleError(err);
    }
  };

  render() {
    const { error, rsaOpened, publicKey, privateKey, sessionKey, text } = this.state;
    const hasRsa = publicKey && privateKey;
    const showText = !!text && !rsaOpened;

    return (
      <View style={styles.container}>
        {error && <Text style={{ color: 'red' }}>{error}</Text>}
        {hasRsa && <DataView {...{ publicKey, privateKey, sessionKey }} />}
        {showText && (
          <ScrollView style={styles.textWrapper}>
            <Text>{text}</Text>
          </ScrollView>
        )}
        <Button
          onPress={this.handleRsaSectionTogle}
          title={`${hasRsa ? 'Reg' : 'G'}enerate rsa keys`}
        />
        {rsaOpened && (
          <View>
            <NumberInput
              label="pass prime p:"
              value={this.state.p}
              onChange={p => this.setState({ p })}
            />
            <NumberInput
              label="pass prime q:"
              value={this.state.q}
              onChange={q => this.setState({ q })}
            />
            <Button onPress={this.generateKeys} title="Submit" />
          </View>
        )}
        {hasRsa && !rsaOpened && !sessionKey && <Button onPress={this.login} title="Login" />}
        {sessionKey && <Button onPress={this.getData} title="Get data" />}
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

  textWrapper: {
    maxHeight: 400,
    margin: 25,
    marginTop: 115,
  },
});
