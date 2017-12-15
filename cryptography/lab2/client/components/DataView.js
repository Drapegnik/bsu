import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 100,
  },
  key: {
    fontSize: 17,
    fontFamily: 'Courier',
    textAlign: 'center',
    lineHeight: 25,
  },
});

export default ({ publicKey, privateKey, sessionKey }) => (
  <View style={styles.container}>
    <Text style={styles.key}>
      Public: ({publicKey.e}, {publicKey.n})
    </Text>
    <Text style={styles.key}>
      Private: ({privateKey.d}, {privateKey.n})
    </Text>
    {sessionKey && <Text style={styles.key}>Session: {sessionKey}</Text>}
  </View>
);
