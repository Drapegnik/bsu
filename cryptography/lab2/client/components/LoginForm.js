import React from 'react';
import { Text, View, TextInput, StyleSheet, Button } from 'react-native';

const styles = StyleSheet.create({
  labelWrapper: {
    marginTop: 10,
    marginBottom: 10,
  },
  label: {
    fontSize: 17,
  },
  input: {
    width: 200,
    margin: 2.5,
    padding: 7.5,
    borderWidth: 1,
    borderColor: 'lightgrey',
    borderRadius: 5,
  },
});

export default ({ user, password, onChange, onSubmit }) => (
  <View>
    <View style={styles.labelWrapper}>
      <Text style={styles.label}>login:</Text>
    </View>
    <TextInput value={user} style={styles.input} onChangeText={user => onChange({ user })} />
    <View style={styles.labelWrapper}>
      <Text style={styles.label}>password:</Text>
    </View>
    <TextInput
      secureTextEntry
      value={password}
      style={styles.input}
      onChangeText={password => onChange({ password })}
    />
    <Button onPress={onSubmit} title="Login" />
  </View>
);
