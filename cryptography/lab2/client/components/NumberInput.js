import React from 'react';
import { Text, View, TextInput, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  labelWrapper: {
    marginTop: 10,
    marginBottom: 10,
  },
  label: {
    fontSize: 17,
  },
  input: {
    width: 100,
    margin: 2.5,
    padding: 7.5,
    borderWidth: 1,
    borderColor: 'lightgrey',
    borderRadius: 5,
  },
});

export default ({ label, value, onChange }) => {
  handleInputChange = text => {
    if (/^\d*$/.test(text)) {
      onChange(text);
    }
  };

  return (
    <View>
      <View style={styles.labelWrapper}>
        <Text style={styles.label}>{label}</Text>
      </View>
      <TextInput
        keyboardType="numeric"
        value={value}
        style={styles.input}
        onChangeText={handleInputChange}
      />
    </View>
  );
};
