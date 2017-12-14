import React from 'react';
import { Text, View, TextInput } from 'react-native';

export default ({ label, value, onChange }) => {
  handleInputChange = text => {
    if (/^\d*$/.test(text)) {
      onChange(text);
    }
  };

  return (
    <View>
      <Text>{label}</Text>
      <TextInput
        keyboardType="numeric"
        value={value}
        style={{ borderColor: 'gray', borderWidth: 1 }}
        onChangeText={handleInputChange}
      />
    </View>
  );
};
