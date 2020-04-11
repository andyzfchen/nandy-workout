import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import CountDown from 'react-native-countdown-component';

export default class TestScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    return (
      <Text> text placeholder </Text>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
