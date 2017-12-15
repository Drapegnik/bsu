import React, { Component } from 'react';
import { StyleSheet, Text, View, Button, TextInput, ScrollView } from 'react-native';

import DataView from './components/DataView';
import NumberInput from './components/NumberInput';
import LoginForm from './components/LoginForm';
import { post, api } from './utils';

global.XMLHttpRequest = global.originalXMLHttpRequest || global.XMLHttpRequest;

export default class App extends Component {
  state = {
    p: '61',
    q: '53',
    user: 'admin',
    password: '',
    publicKey: null,
    privateKey: null,
    sessionKey: null,
    rsaOpened: false,
    text: null,
  };

  handleError = ({ status, error }) => {
    const state = { error, text: null };
    if (status === 401) {
      state.sessionKey = null;
    }
    this.setState(state);
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
      console.log(e, n, d);
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
      const { user, password, publicKey, privateKey } = this.state;
      const { sessionKey } = await post(api.login, {
        user,
        password,
        key: publicKey,
      });
      console.log('encrypted sessionKey: ', sessionKey);

      const { decrypted } = await post(api.private.rsaDecrypt, {
        key: privateKey,
        data: sessionKey,
      });
      console.log('decrypted sessionKey: ', decrypted);
      this.setState({ sessionKey: decrypted, error: null, password: '' });
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
    const {
      user,
      password,
      error,
      rsaOpened,
      publicKey,
      privateKey,
      sessionKey,
      text,
    } = this.state;
    const hasRsaKeys = publicKey && privateKey;
    const showText = !!text && !rsaOpened;
    const showLogin = hasRsaKeys && !rsaOpened && !sessionKey;

    return (
      <View style={styles.container}>
        {error && <Text style={{ color: 'red' }}>{error}</Text>}
        {hasRsaKeys && <DataView {...{ publicKey, privateKey, sessionKey }} />}
        {showText && (
          <ScrollView style={styles.textWrapper}>
            <Text>{text}</Text>
          </ScrollView>
        )}
        {showLogin && (
          <LoginForm
            {...{ user, password }}
            onChange={state => this.setState(state)}
            onSubmit={this.login}
          />
        )}
        <Button
          onPress={this.handleRsaSectionTogle}
          title={`${hasRsaKeys ? 'Reg' : 'G'}enerate rsa keys`}
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
